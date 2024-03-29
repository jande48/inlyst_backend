from django.urls import path
from listing.views import (
    GetListings,
    GetAddresses,
    SetAddress,
    GetChatGPTDescription,
    SetListingValues,
    UploadListingImages,
    UploadListingVideos,
)

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
    path(
        "get_ChatGPT_description/",
        GetChatGPTDescription.as_view(),
        name="get_ChatGPT_description",
    ),
    path(
        "set_listing_values/",
        SetListingValues.as_view(),
        name="set_listing_values",
    ),
    path(
        "upload_listing_photos/",
        UploadListingImages.as_view(),
        name="upload_listing_photos",
    ),
    path(
        "upload_listing_videos/",
        UploadListingVideos.as_view(),
        name="upload_listing_videos",
    ),
]
