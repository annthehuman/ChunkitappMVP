# Generated by Django 3.1.3 on 2020-12-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0030_auto_20201209_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='tehtava',
            field=models.TextField(default=''),
        ),
    ]
