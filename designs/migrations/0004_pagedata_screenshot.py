# Generated by Django 5.1.5 on 2025-02-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0003_image_associatedtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagedata',
            name='screenshot',
            field=models.ImageField(default=1, upload_to='screenshot/'),
            preserve_default=False,
        ),
    ]
