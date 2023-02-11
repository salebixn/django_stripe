from django.urls import path
from .views import (
    Redirect,
    Index,
    Success,
    Cancel,
    BuyItems,
    AddToCart
)


urlpatterns = [
    # Редирект с корня на первый item для удобства
    path('', Redirect.as_view(), name='redirect'),
    # Получение item'ов
    path('item/<id>', Index.as_view(), name='index'),
    # Успешная оплата
    path('success/', Success.as_view(), name='success'),
    # Отмена оплаты
    path('cancel/', Cancel.as_view(), name='cancel'),
    # Получение session.id
    # Без параметра <id> потому что item'ы достаются из сессии
    path('buy/', BuyItems.as_view(), name='create-checkout-session'),
    # Добавление item'а в корзину
    path('addtocart/<id>', AddToCart.as_view(), name='add-to-cart')
]