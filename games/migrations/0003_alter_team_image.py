# Generated by Django 4.2.2 on 2023-07-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_team_image_player_game_bet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='team_pics'),
        ),
    ]
