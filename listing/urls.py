from django.urls import path
from listing.views import (
    GetListings,
    GetAddresses,
    SetAddress,
    GetChatGPTDescription,
    SetListingValues,
    UploadListingImages,
    UploadListingVideos,
    DeleteListingImageOrVideo,
    UpdateWizardStep,
    ResetCoverPhoto
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
    path(
        "delete_listing_photo_or_video/",
        DeleteListingImageOrVideo.as_view(),
        name="delete_listing_photo_or_video",
    ),
     path(
        "reset_cover_photo/",
        ResetCoverPhoto.as_view(),
        name="reset_cover_photo",
    ),
    path(
        "update_wizard_step/",
        UpdateWizardStep.as_view(),
        name="update_wizard_step",
    ),
]
