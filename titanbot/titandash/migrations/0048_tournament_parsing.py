# Generated by Django 2.2.10 on 2020-04-27 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('titandash', '0047_add_summon_dagger_minigame_fixup_forbidden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(blank=True, max_length=255, verbose_name='Rank')),
                ('username', models.CharField(blank=True, max_length=255, verbose_name='Username')),
                ('stage', models.CharField(blank=True, max_length=255, verbose_name='Stage')),
                ('is_user', models.BooleanField(verbose_name='Is User')),
            ],
        ),
        migrations.AddField(
            model_name='configuration',
            name='enable_tournament_parsing',
            field=models.BooleanField(default=True, help_text='Enable the ability to parse out tournament results once tournaments end.', verbose_name='Enable Tournament Parsing'),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255, unique=True, verbose_name='Identifier')),
                ('finished', models.DateTimeField(auto_now_add=True, verbose_name='Finished')),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='titandash.BotInstance', verbose_name='Bot Instance')),
                ('participants', models.ManyToManyField(to='titandash.Participant', verbose_name='Participants')),
            ],
            options={
                'verbose_name': 'Tournament',
                'verbose_name_plural': 'Tournaments',
            },
        ),
    ]
