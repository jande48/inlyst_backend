from django.urls import path
from customer.views import (
    CustomerProfile,
    CustomTokenObtainPairView,
    SignUpView,
    CreateCustomerByPhone,
    VerifyCustomerCode,
    SetPassword
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path(
        "profile/device-id/<str:device_id>/",
        CustomerProfile.as_view(),
        name="customer-profile",
    ),
    path(
        "signup/",
        SignUpView.as_view(),
        name="signup",
    ),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "create_customer_by_phone/<str:phone_number>/<str:device_id>/",
        CreateCustomerByPhone.as_view(),
        name="create_customer_by_phone",
    ),
    path(
        "verify_customer_code/<str:phone_number>/<str:code>/",
        VerifyCustomerCode.as_view(),
        name="verify_customer_code",
    ),
    path(
        "set_password/<str:password>/",
        SetPassword.as_view(),
        name="set_password",
    ),
]
