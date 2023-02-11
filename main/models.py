from django.db import models
from django.contrib.postgres.fields import ArrayField


class Item(models.Model):
    CURRENCY_CHOICES = (
        ('usd', 'USD'),
        ('rub', 'RUB')
    )

    name = models.CharField(max_length=255, null=False, default='Нет названия', verbose_name='Название')
    description = models.TextField(null=False, default='Нет описания', verbose_name='Описание')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, default=0.00, verbose_name='Цена')
    currency = models.CharField(max_length=3, null=False, default='usd', choices=CURRENCY_CHOICES, verbose_name='Валюта')

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class Discount(models.Model):
    percent_off = models.DecimalField(max_digits=4, decimal_places=1, null=False, default=0.0, verbose_name='Процент')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидка'


class Tax(models.Model):
    percent_off = models.IntegerField(null=False, default=0.0, verbose_name='Процент')

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налог'


class Order(models.Model):
    items = ArrayField(models.IntegerField(null=False, default=0), size=10, verbose_name='Заказ')
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, verbose_name='Скидка', blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True, verbose_name='Налог', blank=True)

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


