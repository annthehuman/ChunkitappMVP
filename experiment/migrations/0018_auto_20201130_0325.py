# Generated by Django 3.1.3 on 2020-11-30 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0017_auto_20201130_0307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessions',
            name='session_key_id',
        ),
        migrations.AddField(
            model_name='sessions',
            name='session_key',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]