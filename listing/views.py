from rest_framework.response import Response
from rest_framework.views import APIView


class GetWizardSteps(APIView):

    def get(self, request, device_id=None):
        if not device_id:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )