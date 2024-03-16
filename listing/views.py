from rest_framework.response import Response
from rest_framework.views import APIView
from listing.models import (
    TemplateWizardStep,
    PersonalizedWizardStep,
    Listing,
    ListingThrough,
    TemplateKeyword,
    PersonalizedKeyword,
)
from customer.models import Customer, Credentials, PreciselyAccessToken
from listing.serializers import ListingSerializer
from rest_framework import status, permissions
import requests, re
from customer.utils import get_current_date
from datetime import timedelta
from listing.utils import populate_property_object
from listing.utils import write_to_file


class GetListings(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        customer = Customer.objects.get(pk=request.user.pk)
        listingsThrough = ListingThrough.objects.filter(customer=customer)
        if listingsThrough.count() == 0:
            listing = Listing.objects.create()
            listing_through = ListingThrough.objects.create(
                customer=customer, listing=listing
            )
            template_wizard_steps = TemplateWizardStep.objects.all()
            for template_wizard_step in template_wizard_steps:
                personalized_wizard_step, created = (
                    PersonalizedWizardStep.objects.get_or_create(
                        customer=customer,
                        template_wizard_step=template_wizard_step,
                        listing=listing,
                        name=template_wizard_step.name,
                        subtitle=template_wizard_step.subtitle,
                        index=template_wizard_step.index,
                        num_of_steps=template_wizard_step.num_of_steps,
                    )
                )

        listing_throughs = ListingThrough.objects.filter(customer=customer)
        listings = Listing.objects.filter(
            pk__in=list(listing_throughs.values_list("listing__pk", flat=True))
        )

        return Response(
            {
                "message": "success",
                "listings_unfinished": ListingSerializer(
                    listings.filter(wizard_complete__isnull=True), many=True
                ).data,
                "listings_finished": ListingSerializer(
                    listings.filter(wizard_complete__isnull=False), many=True
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class GetAddresses(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            address_text = request.data["addressText"]
        except:
            address_text = None
        try:
            google_maps_key = Credentials.objects.get(name="google_maps")
        except:
            return Response(
                {"message": "couldnt get google maps key"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            url = f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={address_text}&key={google_maps_key.api_key}"
            response = requests.get(url).json()
        except:
            return Response(
                {"message": "couldnt get google maps api call"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"message": "success", "predictions": response["predictions"]},
            status=status.HTTP_200_OK,
        )


class SetAddress(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            chosenAddress = request.data["chosenAddress"]
        except:
            return Response(
                {"message": "couldnt get chosen addres"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            listingID = request.data["listingID"]
        except:
            return Response(
                {"message": "couldnt get list id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            customer = Customer.objects.get(pk=request.user.pk)
        except:
            return Response(
                {"message": "couldnt get customer"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if (
            PreciselyAccessToken.objects.filter(
                customer=customer, expires_at__gt=get_current_date()
            ).count()
            > 0
        ):
            access_token = (
                PreciselyAccessToken.objects.filter(
                    customer=customer, expires_at__gt=get_current_date()
                )
                .order_by("-expires_at")
                .first()
                .token
            )
        else:
            try:
                precisely_key = (
                    Credentials.objects.filter(name="precisely_key").first().api_key
                )
                precisely_secret = (
                    Credentials.objects.filter(name="precisely_secret").first().api_key
                )
            except:
                return Response(
                    {"message": "couldnt get precisely creds"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            try:
                response = requests.post(
                    "https://api.precisely.com/oauth/token",
                    data={"grant_type": "client_credentials"},
                    auth=(precisely_key, precisely_secret),
                ).json()
            except:
                return Response(
                    {"message": "couldnt get precisely oauth token"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            access_token = response["access_token"]
            PreciselyAccessToken.objects.create(
                token=access_token,
                customer=customer,
                expires_at=(
                    get_current_date() + timedelta(seconds=int(response["expiresIn"]))
                ),
            )

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        try:
            r = requests.get(
                f"https://api.precisely.com/property/v2/attributes/byaddress?address={chosenAddress}&attributes=all",
                headers=headers,
            ).json()
        except:
            return Response(
                {"message": "api call failed to precisely"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        logging_file_path = "logging/address_response_from_precisely.log"
        write_to_file(logging_file_path, f"\n\nResponse from Precisely:\n{r}\n")
        personalized_wizard_step = PersonalizedWizardStep.objects.get(
            customer=customer, template_wizard_step__index=1
        )
        personalized_wizard_step.last_step_completed = 1
        personalized_wizard_step.save()
        listing = Listing.objects.get(pk=listingID)
        try:
            r["propertyAttributes"]["pbKey"]
        except:
            print("there was  problem with pk key \n\n", r)
        pa = r["propertyAttributes"]
        listing = populate_property_object(listing, pa)
        listing.save()

        listing_throughs = ListingThrough.objects.filter(customer=customer)
        listings_unfinished = Listing.objects.filter(
            pk__in=list(listing_throughs.values_list("listing__pk", flat=True)),
            wizard_complete__isnull=True,
        )
        return Response(
            {
                "message": "success",
                "listings_unfinished": ListingSerializer(
                    listings_unfinished, many=True
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class GetChatGPTDescription(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        from openai import OpenAI

        try:
            listingID = request.data["listingID"]
        except:
            return Response(
                {"message": "couldnt get list id"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        listing = Listing.objects.get(pk=listingID)

        if not listing:
            return Response(
                {"message": "couldnt get listing"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        openai_key = Credentials.objects.get(name="chatGPT").api_key
        client = OpenAI(api_key=openai_key)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a poetic assistant, skilled in describing real estate properties with creative flair.",
                },
                {
                    "role": "user",
                    "content": f"Write a description for a {listing.land_use} at {listing.main_address_line}. It has {listing.bedrooms} bedrooms and {listing.baths} with {listing.living_square_footage} living square feet and {listing.property_square_footage} property square feet.  It is located in the {listing.subdivision_name} neighborhood. It was built in {listing.built_year}",
                },
            ],
        )
        description = completion.choices[0].message.content

        return Response(
            {"message": "success", "description": description},
            status=status.HTTP_200_OK,
        )


class SetListingValues(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            listingID = request.data["listingID"]
        except:
            return Response(
                {"message": "couldnt get list id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            listing = Listing.objects.get(pk=listingID)
        except:
            return Response(
                {"message": "couldnt get listing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            sqft = request.data["sqft"]
            listing.square_footage = int(re.sub("\D", "", sqft))
        except:
            pass
        try:
            lotsqft = request.data["lotsqft"]
            listing.living_square_footage = int(re.sub("\D", "", lotsqft))
        except:
            pass
        try:
            bedrooms = request.data["bedrooms"]
            listing.bedrooms = int(bedrooms)
        except:
            pass
        try:
            bathRooms = request.data["bathRooms"]
            listing.baths = bathRooms
        except:
            pass
        try:
            propertyType = request.data["propertyType"]
            listing.property_type = propertyType
        except:
            pass
        try:
            builtYear = request.data["builtYear"]
            listing.built_year = int(re.sub("\D", "", builtYear))
        except:
            pass

        listing.save()

        wizard_index = request.data["wizard_index"]
        last_step_completed = request.data["last_step_completed"]
        PersonalizedWizardStep.objects.filter(
            listing=listing, index=wizard_index
        ).update(last_step_completed=last_step_completed)

        try:
            keyWords = request.data["keyWords"]
        except:
            keyWords = None

        if keyWords and len(keyWords) > 0:
            current_keyword_pks = []
            for keyWord in keyWords:
                try:
                    template_keyword = TemplateKeyword.objects.get(
                        mystatemls_name=keyWord["mystatemls_name"]
                    )
                except:
                    print("Could not get template keyword from this: ", keyWord)
                    continue

                peronalized_keyword, created = (
                    PersonalizedKeyword.objects.get_or_create(
                        listing=listing, template_keyword=template_keyword
                    )
                )
                current_keyword_pks.append(peronalized_keyword.pk)
                PersonalizedKeyword.objects.filter(listing=listing).exclude(
                    pk__in=current_keyword_pks
                ).delete()
        return Response(
            {
                "message": "success",
                "listings_unfinished": ListingSerializer(
                    Listing.objects.filter(pk=listing.pk), many=True
                ).data,
            },
            status=status.HTTP_200_OK,
        )
