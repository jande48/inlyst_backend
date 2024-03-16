from django.contrib import admin
from listing.models import (
    TemplateWizardStep,
    PersonalizedWizardStep,
    Listing,
    ListingThrough,)


admin.site.register(Listing)
admin.site.register(ListingThrough)


@admin.register(TemplateWizardStep)
class TemplateWizardStepAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PersonalizedWizardStep)
class PersonalizedWizardStepAdmin(admin.ModelAdmin):
    list_display = ("name",)
