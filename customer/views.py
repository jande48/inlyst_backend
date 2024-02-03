from rest_framework.response import Response
from rest_framework.views import APIView
from customer.models import Customer
class CustomerProfile(APIView):

    def get(self, request, device_id=None):
        try:
            customer = Customer.objects.get(device_id=str(device_id))
        except:
            customer = Customer.objects.get
        return Response(
            {
                "opt_in_email_alerts": customer.opt_in_email_alerts,
                "opt_in_text_alerts": customer.opt_in_text_alerts,
            }
        )