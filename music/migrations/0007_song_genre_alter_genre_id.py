# Generated by Django 4.1.6 on 2023-02-12 17:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_song_lyric'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.ManyToManyField(to='music.genre'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
