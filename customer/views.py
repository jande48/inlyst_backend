from rest_framework.response import Response
from rest_framework.views import APIView
from customer.models import Device, Credentials, Customer, VerificationCode
from rest_framework import status, permissions
from listing.models import TemplateWizard, PersonalizedWizard
from listing.serializers import PersonalizedWizardSerializer
from customer.serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


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
                "personalized_wizard": PersonalizedWizardSerializer(
                    personalized_wizard, many=True
                ).data,
                "google_maps_key": google_maps_key.api_key,
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
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

        if creation_type == "email" and not email:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )

        if creation_type == "phone":
            customer = Customer.objects.filter(
                phone_number=phone_number.strip()
            ).first()
            if not customer:
                customer = Customer.objects.create(phone_number=phone_number.strip())
        else:
            customer = Customer.objects.filter(email=email.strip()).first()
            if not customer:
                customer = Customer.objects.create(email=email.strip())

        device, created = Device.objects.get_or_create(device_id=str(device_id))
        customer.devices.add(device)
        num_of_digits_for_code = 6
        range_start = 10 ** (num_of_digits_for_code - 1)
        range_end = (10**num_of_digits_for_code) - 1
        verification_code = randint(range_start, range_end)
        VerificationCode.objects.create(customer=customer, code=verification_code)

        # Here is where we would post the verification code to Twilio
        # if creation_type == "phone":
        #     post_code_to_twilio("phone", phone_number, verification_code)
        # else :
        #     post_code_to_twilio("email", email, verification_code)

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

        if not first_name or not last_name:
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
        if email:
            customer.email = email
        customer.save()

        return Response(
            {
                "message": "success",
            },
            status=status.HTTP_200_OK,
        )
