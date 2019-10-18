# Generated by Django 2.2.5 on 2019-10-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titandash', '0017_remove_configuration_bottom_artifact'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='enable_milestones',
            field=models.BooleanField(default=True, help_text='Enable the ability to check and collect milestones in game.', verbose_name='Enable Milestones'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='milestones_check_every_x_hours',
            field=models.PositiveIntegerField(default=1, help_text=['milestones_check_every_x_hours'], verbose_name='Check Milestones Every X Hours'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='milestones_check_on_start',
            field=models.BooleanField(default=False, help_text=['milestones_check_on_start'], verbose_name='Check Milestones On Session Start'),
        ),
    ]