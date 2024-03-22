# Generated by Django 4.2.9 on 2024-03-21 17:15

from django.db import migrations, models
import django.db.models.deletion
import listing.models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0021_alter_photo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('file', models.FileField(max_length=255, upload_to=listing.models.photo_directory_path, verbose_name='File')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_delete', models.DateTimeField(auto_now_add=True, null=True)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file', to='listing.listing')),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
