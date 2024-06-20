from django.urls import path
from customer.views import (
    CustomerProfile,
    CustomTokenObtainPairView,
    SignUpView,
    CreateCustomer,
    VerifyCustomerCode,
    SetPassword,
    UpdateAccount,
    Login,
    GetCustomer,
    ResetListings,
    SendNewCode,
    StripeIdentityVerification
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
        "create_customer/",
        CreateCustomer.as_view(),
        name="create_customer",
    ),
    path(
        "verify_customer_code/",
        VerifyCustomerCode.as_view(),
        name="verify_customer_code",
    ),
    path(
        "set_password/<str:password>/",
        SetPassword.as_view(),
        name="set_password",
    ),
    path(
        "update_account/",
        UpdateAccount.as_view(),
        name="update_account",
    ),
    path(
        "login/",
        Login.as_view(),
        name="login",
    ),
    path(
        "get_customer/",
        GetCustomer.as_view(),
        name="get_customer",
    ),
    path(
        "reset_listings/",
        ResetListings.as_view(),
        name="reset_listings",
    ),
    path(
        "send_new_code/",
        SendNewCode.as_view(),
        name="send_new_code",
    ),
    path(
        "stripe_identity_verification_code/",
        StripeIdentityVerification.as_view(),
        name="stripe_identity_verification_code",
    ),
]
