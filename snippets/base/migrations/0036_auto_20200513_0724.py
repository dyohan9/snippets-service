# Generated by Django 2.2.10 on 2020-05-13 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_remove_target_client_match_rules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fxasignuptemplate',
            name='scene1_section_title_icon',
            field=models.ForeignKey(blank=True, help_text='Section title icon. 64x64px. PNG. scene1_section_title_text must also be specified to display.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fxa_scene1_section_icons', to='base.Icon', verbose_name='Section Title Icon'),
        ),
        migrations.AlterField(
            model_name='newslettertemplate',
            name='scene1_section_title_icon',
            field=models.ForeignKey(blank=True, help_text='Section title icon. 64x64px. PNG. scene1_section_title_text must also be specified to display.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='newsletter_scene1_section_icons', to='base.Icon', verbose_name='Section Title Icon'),
        ),
        migrations.AlterField(
            model_name='sendtodevicetemplate',
            name='scene1_section_title_icon',
            field=models.ForeignKey(blank=True, help_text='Section title icon. 64x64px. PNG. scene1_section_title_text must also be specified to display.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sendtodevice_scene1_section_icons', to='base.Icon', verbose_name='Section Title Icon'),
        ),
        migrations.AlterField(
            model_name='simpletemplate',
            name='section_title_icon',
            field=models.ForeignKey(blank=True, help_text='Section title icon. 64x64px. PNG. section_title_text must also be specified to display.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='simple_section_icons', to='base.Icon', verbose_name='Section Title Icon'),
        ),
    ]
