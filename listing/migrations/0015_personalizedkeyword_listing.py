# Generated by Django 4.2.9 on 2024-03-16 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0014_listing_address_number_listing_appraised_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalizedkeyword',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personalized_keyword', to='listing.listing'),
        ),
    ]
