# Generated by Django 3.1.1 on 2020-11-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0004_auto_20201125_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='url',
            field=models.FileField(blank=True, upload_to='playlist/music'),
        ),
    ]
