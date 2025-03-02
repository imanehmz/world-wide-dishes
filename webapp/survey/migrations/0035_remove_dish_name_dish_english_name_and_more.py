# Generated by Django 5.0.1 on 2024-03-19 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0034_alter_dish_image_alter_dish_ingredients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='name',
        ),
        migrations.AddField(
            model_name='dish',
            name='english_name',
            field=models.CharField(blank=True, help_text="You may leave this blank if the local name of the dish you've provided is in Roman alphabets. If you aren't sure about an English translation for the name, please write a phonetic approximation of how it is pronounced.", max_length=200, verbose_name='What is the name of the dish in English?'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='local_name',
            field=models.CharField(max_length=200, verbose_name='What is the name of the dish (in the local language)?'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='utensils',
            field=models.CharField(blank=True, help_text='For example, knife and fork; hand; chopsticks', max_length=200, verbose_name='What utensils are used to eat this dish? '),
        ),
    ]
