# Generated by Django 5.0.3 on 2024-04-04 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='image_file',
            field=models.ImageField(default='media/default.jpg', upload_to='images/'),
            preserve_default=False,
        ),
    ]
