# Generated by Django 2.2.6 on 2019-12-11 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_dailychannelmetrics_dailycountrymetrics_dailysnippetsmetrics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailySnippetsMetrics',
            new_name='DailySnippetMetrics',
        ),
    ]
