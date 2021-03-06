# Generated by Django 3.1.1 on 2020-11-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='music_text',
            new_name='music_name',
        ),
        migrations.AddField(
            model_name='music',
            name='music_artist',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='music',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
