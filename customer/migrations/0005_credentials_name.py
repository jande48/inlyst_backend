# Generated by Django 4.2.9 on 2024-02-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_credentials_device_remove_customer_device_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='credentials',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
