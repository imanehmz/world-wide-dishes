# Generated by Django 5.0.1 on 2024-03-07 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0021_alter_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='time_of_day',
            field=models.CharField(max_length=255, verbose_name='Time of day'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='type_of_dish',
            field=models.CharField(max_length=255, verbose_name='Type of dish'),
        ),
    ]
