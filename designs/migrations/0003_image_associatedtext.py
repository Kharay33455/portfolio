# Generated by Django 5.1.5 on 2025-02-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0002_remove_pagedata_pic1_remove_pagedata_pic10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='associatedText',
            field=models.TextField(blank=True, null=True),
        ),
    ]
