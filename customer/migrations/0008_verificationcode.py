# Generated by Django 4.2.9 on 2024-02-14 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_rename_device_customer_devices'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
