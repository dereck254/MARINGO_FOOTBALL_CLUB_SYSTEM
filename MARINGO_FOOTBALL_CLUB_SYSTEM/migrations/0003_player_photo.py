# Generated by Django 4.2 on 2023-04-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MARINGO_FOOTBALL_CLUB_SYSTEM', '0002_player_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='photo',
            field=models.ImageField(default=1, max_length=30, upload_to=''),
            preserve_default=False,
        ),
    ]