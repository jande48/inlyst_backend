from django.urls import path
from listing.views import (
    GetWizardSteps
)

urlpatterns = [
    path(
        "get_wizard_steps/",
        GetWizardSteps.as_view(),
        name="get-wizard-steps",
    ),
]