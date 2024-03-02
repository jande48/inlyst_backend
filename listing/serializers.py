from rest_framework import serializers
from listing.models import PersonalizedWizardStep


class PersonalizedWizardStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalizedWizardStep
        fields = [
            "index",
            "name",
            "is_completed",
        ]
