from rest_framework import serializers
from listing.models import PersonalizedWizard


class PersonalizedWizardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalizedWizard
        fields = [
            "index",
            "name",
            "is_completed",
        ]
