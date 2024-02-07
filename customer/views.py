from rest_framework.response import Response
from rest_framework.views import APIView
from customer.models import Device, Credentials
from rest_framework import status
from listing.models import TemplateWizard, PersonalizedWizard
from listing.serializers import PersonalizedWizardSerializer

class CustomerProfile(APIView):

    def get(self, request, device_id=None):
        if not device_id:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
        device, created = Device.objects.get_or_create(device_id=str(device_id))
        template_wizards = TemplateWizard.objects.all()
        for template_wizard in template_wizards:
            personalized_wizard, created = PersonalizedWizard.objects.get_or_create(
                device=device, template_wizard=template_wizard
            )
        personalized_wizard = PersonalizedWizard.objects.filter(device=device)
        google_maps_key = Credentials.objects.get(name="google_maps")

        return Response(
            {
                "personalized_wizard": PersonalizedWizardSerializer(personalized_wizard,many=True).data,
                "google_maps_key": google_maps_key.api_key
            }
        )
