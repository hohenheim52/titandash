# Generated by Django 2.2.5 on 2019-10-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titandash', '0021_enable_disable_ad_configuration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='activate_skills_on_start',
            field=models.BooleanField(default=True, help_text='Should skills be activated once when a session is started.', verbose_name='Activate Skills On Session Start'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='daily_achievements_check_on_start',
            field=models.BooleanField(default=False, help_text='Should daily achievements be checked for completion when a session is started.', verbose_name='Check Daily Achievements On Session Start'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='enable_premium_ad_collect',
            field=models.BooleanField(default=False, help_text='Enable the premium ad collection, Note: This will only work if you have unlocked the ability to skip ads, leave disabled to watch ads.', verbose_name='Enable Premium Ad Collection'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='max_skill_if_possible',
            field=models.BooleanField(default=True, help_text="Should a skill be levelled to it's maximum available amount if the option is present when levelling.", verbose_name='Max Skill If Possible'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='milestones_check_on_start',
            field=models.BooleanField(default=False, help_text='Should milestones be checked for completion when a session is started.', verbose_name='Check Milestones On Session Start'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='prestige_at_max_stage_percent',
            field=models.DecimalField(decimal_places=3, default=0, help_text='Determine if you would like to perform an automatic prestige once a certain percent of your max stage has been reached. You may use values larger than 100 here to push your max stage. (ie: 99, 99.5, 101) (0 = off).', max_digits=255, verbose_name='Prestige At Max Stage Percent'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='prestige_x_minutes',
            field=models.PositiveIntegerField(default=45, help_text="Determine the amount of minutes between each auto prestige process. This can be used for farming, or as a hard limit that is used if the thresholds below aren't met within this time limit. (0 = off).", verbose_name='Prestige In X Minutes'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='raid_notifications_twilio_to_number',
            field=models.CharField(blank=True, help_text='Specify the phone number you would like to receive notifications at (ex: +19991234567)', max_length=255, null=True, verbose_name='Raid Notifications Twilio To Number'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='run_actions_on_start',
            field=models.BooleanField(default=False, help_text='Should all enabled actions be executed once when a session is started.', verbose_name='Run Actions On Session Start'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='soft_shutdown_update_stats',
            field=models.BooleanField(default=True, help_text='Perform a stats update when a soft shutdown is executed.', verbose_name='Update Stats On Soft Shutdown'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='upgrade_artifacts',
            field=models.ManyToManyField(blank=True, help_text='Should any artifacts be specifically upgraded, disabling the above settings and choosing an artifact here will only upgrade the selected artifact(s).', related_name='upgrade_artifacts', to='titandash.Artifact', verbose_name='Upgrade Artifacts'),
        ),
    ]
