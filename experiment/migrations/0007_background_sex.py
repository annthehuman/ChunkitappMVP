# Generated by Django 3.1.3 on 2020-11-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0006_auto_20201127_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='sex',
            field=models.CharField(choices=[('Mies', 'Mies'), ('Nainen', 'Nainen'), ('Muu', 'Muu')], default='Mies', max_length=6),
        ),
    ]