# Generated by Django 4.2 on 2024-03-31 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_categories_slug_todo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Обьявление', 'verbose_name_plural': 'Обьявления'},
        ),
    ]
