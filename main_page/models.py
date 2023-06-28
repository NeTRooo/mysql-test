from django.db import models
from django.contrib.auth.models import User

# user, nick, access, prime, pay, pay_id
class BuyStatus(models.Model):

    user = models.ManyToManyField(User, verbose_name='Пользователь')
    email = models.TextField(verbose_name='почта пользователя')
    nick = models.CharField(max_length=16, verbose_name='Ник игрока.')
    uid = models.TextField(verbose_name='uid дискорд')
    access = models.CharField(max_length=32, verbose_name='Что покупает.')
    prime = models.CharField(max_length=16, verbose_name='Prime подписка.')
    pay = models.CharField(max_length=16, verbose_name='Оплатил?')
    pay_id = models.TextField(verbose_name='ID покупки')

    class Meta:
        verbose_name = 'Инфо о покупках проходки'
        verbose_name_plural = 'Инфо о покупках проходкок'

# user email nick pay_id start_date end_date
class PrimeStatus(models.Model):
    
    user = models.ManyToManyField(User, verbose_name='Пользователь')
    email = models.TextField(verbose_name='Почта пользователя')
    nick = models.CharField(max_length=16, verbose_name='Ник игрока.')
    pay_id = models.TextField(verbose_name='ID покупки')
    start_date = models.DateField(verbose_name='Дата покупки')
    end_date = models.DateField(verbose_name='Дата окончания')
    
    class Meta:
        verbose_name = 'Покупка прайма'
        verbose_name_plural = 'Покупки прайма'
