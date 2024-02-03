from django.urls import path
# from . import views
from customer.views import (
    CustomerProfile
)


urlpatterns = [
    path("profile/device-id/<str:device_id>/", CustomerProfile.as_view(), name="customer-profile"),
]