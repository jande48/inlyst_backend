from django.db import models
from django.db.models import CharField, IntegerField, BooleanField, DateTimeField
from customer.utils import get_current_date


class TemplateWizard(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    name = CharField(max_length=255, null=True, blank=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(TemplateWizard, self).save(*args, **kwargs)


class PersonalizedWizard(models.Model):
    created_at = DateTimeField(auto_now_add=True, null=True, blank=True)
    index = IntegerField(null=True, default=0)
    name = CharField(max_length=255, null=True, blank=True)
    is_completed = DateTimeField(null=True, blank=True)

    def save(
        self,
        *args,
        **kwargs,
    ):
        if not self.created_at:
            self.created_at = get_current_date()
        super(PersonalizedWizard, self).save(*args, **kwargs)
