# Generated by Django 4.2 on 2024-03-09 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(unique=True, verbose_name='ID telegram')),
                ('name', models.TextField(verbose_name='Имя пользователя')),
                ('username', models.TextField(verbose_name='username')),
                ('block', models.TextField(default='no', verbose_name='Блокировка')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(verbose_name='ID telegram')),
                ('text', models.TextField(verbose_name='Текст')),
                ('answer', models.TextField(blank=True, verbose_name='Ответ')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Время получения')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.message')),
            ],
            options={
                'verbose_name': 'Фильтр',
                'verbose_name_plural': 'Фильтры',
            },
        ),
    ]
