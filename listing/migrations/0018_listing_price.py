# Generated by Django 4.2.9 on 2024-03-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0017_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.TextField(blank=True, null=True),
        ),
    ]
