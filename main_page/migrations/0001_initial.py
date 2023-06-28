# Generated by Django 4.2.2 on 2023-06-28 20:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(verbose_name='Почта пользователя')),
                ('nick', models.CharField(max_length=16, verbose_name='Ник игрока.')),
                ('pay_id', models.TextField(verbose_name='ID покупки')),
                ('start_date', models.DateField(verbose_name='Дата покупки')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Покупка прайма',
                'verbose_name_plural': 'Покупки прайма',
            },
        ),
        migrations.CreateModel(
            name='BuyStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(verbose_name='почта пользователя')),
                ('nick', models.CharField(max_length=16, verbose_name='Ник игрока.')),
                ('uid', models.TextField(verbose_name='uid дискорд')),
                ('access', models.CharField(max_length=32, verbose_name='Что покупает.')),
                ('prime', models.CharField(max_length=16, verbose_name='Prime подписка.')),
                ('pay', models.CharField(max_length=16, verbose_name='Оплатил?')),
                ('pay_id', models.TextField(verbose_name='ID покупки')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Инфо о покупках проходки',
                'verbose_name_plural': 'Инфо о покупках проходкок',
            },
        ),
    ]
