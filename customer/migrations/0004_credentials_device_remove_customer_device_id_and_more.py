# Generated by Django 4.2.9 on 2024-02-05 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_device_id_alter_baseuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('api_key', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('customer.baseuser',),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_test', models.BooleanField(default=False)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('customer.baseuser',),
        ),
        migrations.RemoveField(
            model_name='customer',
            name='device_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='device',
            field=models.ManyToManyField(to='customer.device'),
        ),
    ]
