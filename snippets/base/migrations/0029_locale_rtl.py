# Generated by Django 2.2.6 on 2019-12-16 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_target_filtr_needs_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='locale',
            name='rtl',
            field=models.BooleanField(default=False, help_text='Is Right-To-Left language?'),
        ),
    ]
