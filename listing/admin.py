from django.contrib import admin
from listing.models import (
    TemplateWizardStep,
    PersonalizedWizardStep,
    Listing,
    ListingThrough,
    Property,
)


admin.site.register(Listing)
admin.site.register(ListingThrough)
admin.site.register(Property)


@admin.register(TemplateWizardStep)
class TemplateWizardStepAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PersonalizedWizardStep)
class PersonalizedWizardStepAdmin(admin.ModelAdmin):
    list_display = ("name",)
