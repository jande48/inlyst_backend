# Generated by Django 4.2.9 on 2024-03-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0025_rename_last_index_shown_personalizedwizardstep_last_step_shown'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price_per_sqft',
            field=models.IntegerField(null=True),
        ),
    ]