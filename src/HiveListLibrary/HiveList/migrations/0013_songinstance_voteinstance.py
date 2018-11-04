# Generated by Django 2.1.1 on 2018-11-04 04:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('HiveList', '0012_remove_playlist_playlist_vote_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongInstance',
            fields=[
                ('song_instance_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular Song Instance', primary_key=True, serialize=False)),
                ('number_yes_votes', models.IntegerField(default=0)),
                ('number_no_votes', models.IntegerField(default=0)),
                ('contributor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HiveList.Contributor')),
                ('playlist_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HiveList.Playlist')),
                ('song_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HiveList.Song')),
            ],
        ),
        migrations.CreateModel(
            name='VoteInstance',
            fields=[
                ('vote_instance_id', models.IntegerField(primary_key=True, serialize=False)),
                ('vote', models.CharField(blank=True, choices=[('y', 'yes'), ('n', 'no')], max_length=1)),
                ('contributor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HiveList.Contributor')),
                ('playlist_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HiveList.Playlist')),
                ('song_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HiveList.SongInstance')),
            ],
        ),
    ]