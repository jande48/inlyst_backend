from django.contrib import admin
from listing.models import TemplateWizardStep, PersonalizedWizardStep


@admin.register(TemplateWizardStep)
class TemplateWizardStepAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PersonalizedWizardStep)
class PersonalizedWizardStepAdmin(admin.ModelAdmin):
    list_display = ("name",)
