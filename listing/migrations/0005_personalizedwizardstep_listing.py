# Generated by Django 4.2.9 on 2024-03-03 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0004_rename_template_wizard_personalizedwizardstep_template_wizard_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalizedwizardstep',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personalized_wizard', to='listing.listing'),
        ),
    ]
