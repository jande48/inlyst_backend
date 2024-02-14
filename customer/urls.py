from django.urls import path
from customer.views import CustomerProfile, CustomTokenObtainPairView, SignUpView
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
]
