from django.contrib import admin
from listing.models import TemplateWizard, PersonalizedWizard


@admin.register(TemplateWizard)
class TemplateWizardAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PersonalizedWizard)
class PersonalizedWizardAdmin(admin.ModelAdmin):
    list_display = ("name",)
