# Generated by Django 4.2.9 on 2024-03-30 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0024_personalizedwizardstep_last_index_shown_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalizedwizardstep',
            old_name='last_index_shown',
            new_name='last_step_shown',
        ),
    ]