# Generated by Django 4.2.9 on 2024-03-10 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_preciselyaccesstoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='preciselyaccesstoken',
            name='expires_in_seconds',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]