# Generated by Django 5.2 on 2025-05-05 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_gallery_galleryitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryitem',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_items', to='core.gallery'),
        ),
    ]
