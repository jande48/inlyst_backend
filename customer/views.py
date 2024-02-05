from rest_framework.response import Response
from rest_framework.views import APIView
from customer.models import Device
from rest_framework import status
from listing.models import TemplateWizard, PersonalizedWizard


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

        return Response(
            {
                "message": "success",
            }
        )
