# Generated by Django 2.2.3 on 2019-09-16 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20190911_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='distributions',
        ),
        migrations.AlterField(
            model_name='job',
            name='distribution',
            field=models.ForeignKey(default=1, help_text='Set a Distribution for this Job. It should be normally left to Default. Useful for running Normandy experiments.', on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='base.Distribution'),
            preserve_default=False,
        ),
    ]
