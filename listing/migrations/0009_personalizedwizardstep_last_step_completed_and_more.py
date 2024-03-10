# Generated by Django 4.2.9 on 2024-03-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_alter_personalizedwizardstep_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalizedwizardstep',
            name='last_step_completed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personalizedwizardstep',
            name='num_of_steps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='templatewizardstep',
            name='num_of_steps',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
