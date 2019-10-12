# Generated by Django 2.2.5 on 2019-10-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titandash', '0023_memu_emulator_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='master_level_only_once',
            field=models.BooleanField(default=False, help_text='Enable the option to only level the sword master once at the beginning of a session, and once after every prestige.', verbose_name='Level Sword Master Once Per Prestige'),
        ),
    ]
