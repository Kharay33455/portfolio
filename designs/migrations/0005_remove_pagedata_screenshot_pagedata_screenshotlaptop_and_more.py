# Generated by Django 5.1.5 on 2025-02-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0004_pagedata_screenshot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagedata',
            name='screenshot',
        ),
        migrations.AddField(
            model_name='pagedata',
            name='screenshotLaptop',
            field=models.ImageField(default=1, upload_to='screenshot/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagedata',
            name='screenshotPhone',
            field=models.ImageField(default=1, upload_to='screenshot/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagedata',
            name='screenshotiPad',
            field=models.ImageField(default=1, upload_to='screenshot/'),
            preserve_default=False,
        ),
    ]
