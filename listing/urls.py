from django.urls import path
from listing.views import GetListings, GetAddresses

urlpatterns = [
    path(
        "get_listings/",
        GetListings.as_view(),
        name="get-listings",
    ),
    path(
        "get_addresses/",
        GetAddresses.as_view(),
        name="get-get_addresses",
    ),
]
