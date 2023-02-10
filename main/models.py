from django.db import models


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