from django.urls import path
from .views import (
    index,
    success,
    cancel,
    CreateCheckoutSessionView
)


urlpatterns = [
    path('item/<id>', index, name='index'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('buy/<id>', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]