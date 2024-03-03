from rest_framework import serializers
from listing.models import PersonalizedWizardStep, Listing, Listing


class PersonalizedWizardStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalizedWizardStep
        fields = [
            "pk",
            "index",
            "name",
            "subtitle",
            "is_completed",
        ]


class ListingSerializer(serializers.ModelSerializer):
    def get_wizard_steps(self, obj):
        steps = PersonalizedWizardStep.objects.filter(listing__pk=obj.pk)
        return PersonalizedWizardStepSerializer(steps, many=True).data

    wizard_steps = serializers.SerializerMethodField(method_name="get_wizard_steps")

    class Meta:
        model = Listing
        fields = ["pk", "wizard_steps", "wizard_complete"]
