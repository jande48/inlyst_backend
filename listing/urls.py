from django.urls import path
from listing.views import GetListings

urlpatterns = [
    path(
        "get_listings/",
        GetListings.as_view(),
        name="get-listings",
    ),
]
