from django.urls import path
from listing.views import GetListings, GetAddresses,SetAddress

urlpatterns = [
    path(
        "get_listings/",
        GetListings.as_view(),
        name="get-listings",
    ),
    path(
        "get_addresses/",
        GetAddresses.as_view(),
        name="get_addresses",
    ),
    path(
        "set_address_to_listing/",
        SetAddress.as_view(),
        name="set_addresses",
    ),
]
