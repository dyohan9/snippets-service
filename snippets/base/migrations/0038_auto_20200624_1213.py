# Generated by Django 2.2.13 on 2020-06-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_auto_20200604_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobdailyperformance',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='adj_impression_no_clients',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='adj_impression_no_clients_total',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='block_no_clients',
            field=models.PositiveIntegerField(default=0, editable=False, help_text='Must be equal or close to `block`'),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='block_no_clients_total',
            field=models.PositiveIntegerField(default=0, editable=False, help_text='Must be equal or close to `block`'),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='click_no_clients',
            field=models.PositiveIntegerField(default=0, editable=False, help_text='Must be equal or close to `click`.'),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='click_no_clients_total',
            field=models.PositiveIntegerField(default=0, editable=False, help_text='Must be equal or close to `click`.'),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='dismiss_no_clients',
            field=models.PositiveIntegerField(default=0, editable=False, help_text='Must be equal or close to `dismiss`'),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='dismiss_no_clients_total',
            field=models.PositiveIntegerField(default=0, editable=False, help_text='Must be equal or close to `dismiss`'),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='go_to_scene2_no_clients',
            field=models.PositiveIntegerField(default=0, editable=False, help_text='Must be equal or close to `go_to_scene2`'),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='go_to_scene2_no_clients_total',
            field=models.PositiveIntegerField(default=0, editable=False, help_text='Must be equal or close to `go_to_scene2`'),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='impression_no_clients',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='impression_no_clients_total',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='other_click_no_clients',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='other_click_no_clients_total',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='subscribe_error_no_clients',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='subscribe_error_no_clients_total',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='subscribe_success_no_clients',
            field=models.PositiveIntegerField(default=0, editable=False, help_text='Must be equal or close to `subscribe_success`'),
        ),
        migrations.AddField(
            model_name='jobdailyperformance',
            name='subscribe_success_no_clients_total',
            field=models.PositiveIntegerField(default=0, editable=False, help_text='Must be equal or close to `subscribe_success`'),
        ),
    ]
