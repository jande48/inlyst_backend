from rest_framework.response import Response
from rest_framework.views import APIView
from customer.models import Device, Customer, VerificationCode
from listing.models import PersonalizedWizardStep, ListingThrough, Listing
from rest_framework import status, permissions
from customer.serializers import CustomerSerializer
from customer.serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from dateutil import parser
from customer.utils import get_current_date
from listing.serializers import ListingSerializer
from listing.utils import create_new_listing


class CustomerProfile(APIView):

    def get(self, request, device_id=None):
        if not device_id:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
        device, created = Device.objects.get_or_create(device_id=str(device_id))

        return Response(
            {
                "message": "success",
            }
        )


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class SignUpView(APIView):

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        if not email or not password or len(password) < 6:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

        customer = Customer(email=email)
        customer.set_password(password)
        customer.save()

        refresh = RefreshToken.for_user(customer)

        return Response(
            {
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            }
        )


class CreateCustomer(APIView):

    def post(self, request):
        from random import randint

        try:
            email = request.data["email"]
        except:
            email = None
        try:
            device_id = request.data["device_id"]
        except:
            device_id = None
        try:
            phone_number = request.data["phoneNumber"]
        except:
            phone_number = None
        try:
            creation_type = request.data["creation_type"]
        except:
            creation_type = None
        if not creation_type or not device_id:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

        if creation_type not in ["phone", "email"]:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

        if creation_type == "phone" and not phone_number:
            return Response({"message": "Please enter a Phone Number"})

        if creation_type == "email" and not email:
            return Response({"message": "Please enter an Email"})

        if creation_type == "phone":
            customer, created = Customer.objects.get_or_create(
                phone_number=phone_number.strip()
            )
            if not created:
                return Response({"message": "That Phone Number is taken"})
        else:
            customer, created = Customer.objects.get_or_create(email=email.strip())
            if not created:
                Response({"message": "That Email is taken"})

        device, created = Device.objects.get_or_create(device_id=str(device_id))
        customer.devices.add(device)
        num_of_digits_for_code = 6
        range_start = 10 ** (num_of_digits_for_code - 1)
        range_end = (10**num_of_digits_for_code) - 1
        verification_code = randint(range_start, range_end)
        VerificationCode.objects.create(customer=customer, code=verification_code)

        # Here is where we would post the verification code to Twilio
        # if creation_type == "phone":
        #     post_code_to_twilio(phone_number, verification_code)
        # else :
        #     post_code_to_sendgrid( email, verification_code)

        return Response({"message": "success"})


class VerifyCustomerCode(APIView):

    def post(self, request):
        try:
            email = request.data["email"]
        except:
            email = None
        try:
            verificationType = request.data["verificationType"]
        except:
            verificationType = None
        try:
            phone_number = request.data["phoneNumber"]
        except:
            phone_number = None
        try:
            verificationCode = request.data["verificationCode"]
        except:
            verificationCode = None

        if not verificationType or not verificationCode:
            return Response(
                {"message": "fail"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if verificationType not in ["phone", "email"]:
            return Response(
                {"message": "fail"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if verificationType == "phone" and not phone_number:
            return Response(
                {"message": "fail"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if verificationType == "email" and not email:
            return Response(
                {"message": "fail"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            if verificationType == "phone":
                customer = Customer.objects.get(phone_number=phone_number.strip())
            else:
                customer = Customer.objects.get(email=email.strip())
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
        code_obj = (
            VerificationCode.objects.filter(customer=customer)
            .order_by("-created_at")
            .first()
        )
        if not code_obj:
            return Response(
                {"message": "fail"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if str(verificationCode) != str(code_obj.code):
            return Response(
                {"message": "fail"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        customer.verified_phone_or_email = get_current_date()
        customer.save()
        refresh = RefreshToken.for_user(customer)
        return Response(
            {
                "message": "success",
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )


class SetPassword(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, password=None):

        if not password:
            return Response(
                {"message": "fail"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            customer = request.user
            if not customer:
                raise Exception("No customer")
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

        customer.set_password(password)
        customer.save()

        return Response(
            {"message": "success"},
            status=status.HTTP_200_OK,
        )


class UpdateAccount(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            email = request.data["email"]
        except:
            email = None
        try:
            first_name = request.data["firstName"]
        except:
            first_name = None
        try:
            last_name = request.data["lastName"]
        except:
            last_name = None
        try:
            birthday = parser.parse(request.data["birthday"])
        except:
            birthday = None
        try:
            phone_number = parser.parse(request.data["phoneNumber"])
        except:
            phone_number = None

        if not first_name or not last_name or not birthday:
            return Response(
                {"message": "fail"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            customer = request.user
            if not customer:
                raise Exception("No customer")
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

        customer.first_name = first_name
        customer.last_name = last_name
        customer.birthday = birthday
        customer.completed_signup = get_current_date()
        if email:
            customer.email = email
        if phone_number:
            customer.phone_number
        customer.save()

        return Response(
            {
                "message": "success",
                "customer": CustomerSerializer(customer, many=False).data,
            },
            status=status.HTTP_200_OK,
        )


class Login(APIView):

    def post(self, request):
        try:
            email_or_phone = request.data["emailOrPhone"]
        except:
            email_or_phone = None
        try:
            password = request.data["password"]
        except:
            password = None

        if not email_or_phone:
            print("returning no email or phoen")
            return Response(
                {"message": "No phone or email provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not password:
            print("returning no password")
            return Response(
                {"message": "No password provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            customer = Customer.objects.get(email=email_or_phone)
        except:
            try:
                customer = Customer.objects.get(phone_number=email_or_phone)
            except:
                print("returning now customer")
                return Response(
                    {"message": "No customer with that phone/email"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if customer.check_password(password.strip()):
            refresh = RefreshToken.for_user(customer)
            return Response(
                {
                    "message": "success",
                    "refresh_token": str(refresh),
                    "access_token": str(refresh.access_token),
                    "customer": CustomerSerializer(customer, many=False).data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "message": "Incorrect password",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class GetCustomer(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        customer = Customer.objects.get(pk=request.user.pk)
        try:
            refresh = RefreshToken.for_user(customer)
            return Response(
                {
                    "message": "success",
                    "customer": CustomerSerializer(customer, many=False).data,
                    "refresh_token": str(refresh),
                    "access_token": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print("the error with GetCustomer is ", e)
            return Response(
                {"message": "failure"},
                status=status.HTTP_200_OK,
            )


class ResetListings(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        customer = Customer.objects.get(pk=request.user.pk)
        PersonalizedWizardStep.objects.filter(customer=customer).delete()
        listing_throughs = ListingThrough.objects.filter(customer=customer)
        listing_pks = []
        for listing_through in listing_throughs:
            if listing_through.listing.pk not in listing_pks:
                listing_pks.append(listing_through.pk)
        Listing.objects.filter(pk__in=listing_pks).delete()

        create_new_listing(customer)

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
            },
            status=status.HTTP_200_OK,
        )
