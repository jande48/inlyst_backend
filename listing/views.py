from rest_framework.response import Response
from rest_framework.views import APIView
from listing.models import (
    TemplateWizardStep,
    PersonalizedWizardStep,
    Listing,
    ListingThrough,
)
from customer.models import Customer
from listing.serializers import ListingSerializer
from rest_framework import status, permissions


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
                    )
                )

        listing_throughs = ListingThrough.objects.filter(customer=customer)
        listings = Listing.objects.filter(
            pk__in=list(listing_throughs.values_list("listing__pk", flat=True))
        )

        return Response(
            {
                "message": "success",
                "listings_unfinished": ListingSerializer(listings.filter(wizard_complete__isnull=True), many=True).data,
                "listings_finished": ListingSerializer(listings.filter(wizard_complete__isnull=False), many=True).data,
            },
            status=status.HTTP_200_OK,
        )
