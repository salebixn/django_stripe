# Generated by Django 4.1.6 on 2023-02-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_tax_alter_order_discount_order_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='percent_off',
            field=models.IntegerField(default=0.0, verbose_name='Процент'),
        ),
    ]
