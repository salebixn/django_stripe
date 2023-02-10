# Generated by Django 4.1.6 on 2023-02-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Нет названия', max_length=255, verbose_name='Название')),
                ('description', models.TextField(default='Нет описания', verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
