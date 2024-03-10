# Generated by Django 4.2.9 on 2024-03-10 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0009_personalizedwizardstep_last_step_completed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property', to='listing.listing')),
            ],
        ),
    ]
