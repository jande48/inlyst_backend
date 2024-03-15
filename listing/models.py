from django.db import models
from django.db.models import (
    CharField,
    IntegerField,
    BooleanField,
    DateTimeField,
    CASCADE,
    ForeignKey,
    TextField,
)
from customer.utils import get_current_date
from customer.models import Customer


class Listing(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    wizard_complete = DateTimeField(null=True, blank=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(Listing, self).save(*args, **kwargs)


class ListingThrough(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    listing = ForeignKey(
        Listing,
        on_delete=CASCADE,
        related_name="listing_through",
        null=True,
    )
    customer = ForeignKey(
        Customer,
        on_delete=CASCADE,
        related_name="listing_through",
        null=True,
    )

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(ListingThrough, self).save(*args, **kwargs)


class TemplateWizardStep(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    index = IntegerField(null=True, blank=True)
    name = CharField(max_length=255, null=True, blank=True)
    subtitle = TextField(null=True, blank=True)
    num_of_steps = IntegerField(null=True, blank=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(TemplateWizardStep, self).save(*args, **kwargs)


class PersonalizedWizardStep(models.Model):
    template_wizard_step = ForeignKey(
        TemplateWizardStep,
        on_delete=CASCADE,
        related_name="personalized_wizard",
        null=True,
    )
    customer = ForeignKey(
        Customer, on_delete=CASCADE, related_name="personalized_wizard", null=True
    )
    listing = ForeignKey(
        Listing, on_delete=CASCADE, related_name="personalized_wizard", null=True
    )
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    index = IntegerField(null=True, default=0)
    name = CharField(max_length=255, null=True, blank=True)
    num_of_steps = IntegerField(null=True, blank=True)
    last_step_completed = IntegerField(null=True, blank=True)
    is_completed = DateTimeField(null=True, blank=True)
    subtitle = TextField(null=True, blank=True)
    index = IntegerField(null=True, blank=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        if not self.last_step_completed:
            self.last_step_completed = 0
        super(PersonalizedWizardStep, self).save(*args, **kwargs)


class Property(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    pbKey = TextField(null=True, blank=True)
    property_type = TextField(null=True, blank=True)
    building_type = TextField(null=True, blank=True)
    square_footage = IntegerField(null=True, blank=True)
    living_square_footage = IntegerField(null=True, blank=True)
    property_square_footage = IntegerField(null=True, blank=True)
    parking_square_footage = IntegerField(null=True, blank=True)
    property_acres = TextField(null=True, blank=True)
    land_use = TextField(null=True, blank=True)
    roof_cover_type = TextField(null=True, blank=True)
    subdivision_name = TextField(null=True, blank=True)
    built_year = IntegerField(null=True, blank=True)
    effective_built_year = IntegerField(null=True, blank=True)
    bedrooms = IntegerField(null=True, blank=True)
    baths = TextField(null=True, blank=True)
    partial_baths = TextField(null=True, blank=True)
    mobile_home = BooleanField(null=True)
    cooling_type = TextField(null=True, blank=True)
    assessed_value = IntegerField(null=True, blank=True)
    market_value = IntegerField(null=True, blank=True)
    appraised_value = IntegerField(null=True, blank=True)
    tax_amount = TextField(null=True, blank=True)
    sales_date = TextField(null=True, blank=True)
    prior_sales_date = TextField(null=True, blank=True)
    foundation = TextField(null=True, blank=True)
    tax_address = TextField(null=True, blank=True)
    main_address_line = TextField(null=True, blank=True)
    address_number = TextField(null=True, blank=True)
    street_name = TextField(null=True, blank=True)
    street_type = TextField(null=True, blank=True)
    city = TextField(null=True, blank=True)
    state = TextField(null=True, blank=True)
    post_code_1 = TextField(null=True, blank=True)
    post_code_2 = TextField(null=True, blank=True)
    vacancy = TextField(null=True, blank=True)
    owner_first_name = TextField(null=True, blank=True)
    owner_middle_name = TextField(null=True, blank=True)
    owner_last_name = TextField(null=True, blank=True)
    owner_type = TextField(null=True, blank=True)

    listing = ForeignKey(Listing, on_delete=CASCADE, related_name="property", null=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(Property, self).save(*args, **kwargs)


class TemplateKeyword(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    name = CharField(max_length=255, null=True, blank=True)
    mystatemls_name = CharField(max_length=255, null=True, blank=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(TemplateKeyword, self).save(*args, **kwargs)


class PersonalizedKeyword(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    name = CharField(max_length=255, null=True, blank=True)
    mystatemls_name = CharField(max_length=255, null=True, blank=True)
    template_keyword = ForeignKey(
        TemplateKeyword,
        on_delete=CASCADE,
        related_name="personalized_keyword",
        null=True,
    )

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(PersonalizedKeyword, self).save(*args, **kwargs)
