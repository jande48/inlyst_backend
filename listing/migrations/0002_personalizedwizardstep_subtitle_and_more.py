# Generated by Django 4.2.9 on 2024-03-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalizedwizardstep',
            name='subtitle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='templatewizardstep',
            name='subtitle',
            field=models.TextField(blank=True, null=True),
        ),
    ]
