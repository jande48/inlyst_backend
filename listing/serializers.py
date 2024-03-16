from rest_framework import serializers
from listing.models import PersonalizedWizardStep, Listing


class PersonalizedWizardStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalizedWizardStep
        fields = [
            "pk",
            "index",
            "name",
            "subtitle",
            "is_completed",
            "num_of_steps",
            "last_step_completed",
        ]


class ListingSerializer(serializers.ModelSerializer):
    def get_wizard_steps(self, obj):
        steps = PersonalizedWizardStep.objects.filter(listing__pk=obj.pk).order_by(
            "index"
        )
        return PersonalizedWizardStepSerializer(steps, many=True).data

    wizard_steps = serializers.SerializerMethodField(method_name="get_wizard_steps")

    class Meta:
        model = Listing
        fields = [
            "pk",
            "wizard_steps",
            "wizard_complete",
            "pk",
            "pbKey",
            "property_type",
            "building_type",
            "square_footage",
            "living_square_footage",
            "property_square_footage",
            "parking_square_footage",
            "property_acres",
            "land_use",
            "roof_cover_type",
            "subdivision_name",
            "built_year",
            "effective_built_year",
            "bedrooms",
            "baths",
            "partial_baths",
            "mobile_home",
            "cooling_type",
            "assessed_value",
            "market_value",
            "appraised_value",
            "tax_amount",
            "sales_date",
            "prior_sales_date",
            "foundation",
            "tax_address",
            "main_address_line",
            "address_number",
            "street_name",
            "street_type",
            "city",
            "state",
            "post_code_1",
            "post_code_2",
            "vacancy",
            "owner_first_name",
            "owner_middle_name",
            "owner_last_name",
            "owner_type",
        ]
