# Generated by Django 4.2.9 on 2024-03-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0022_file_delete_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='is_delete',
        ),
        migrations.AddField(
            model_name='file',
            name='is_cover_photo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='is_deleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='order',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
