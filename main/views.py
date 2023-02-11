import os

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Item, Order

import stripe


class Redirect(View):
    def get(self, request, *args, **kwarg):
        return redirect('/item/1')


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(pk=self.kwargs["id"])
        context = super(Index, self).get_context_data(**kwargs)

        try:
            context.update({
                "item": item,
                "STRIPE_PUBLISHABLE_KEY": os.getenv('STRIPE_PUBLISHABLE_KEY'),
                "count_order": int(tuple(self.request.session.values())[-1])
            })
        except:
            context.update({
                "item": item,
                "STRIPE_PUBLISHABLE_KEY": os.getenv('STRIPE_PUBLISHABLE_KEY'),
                "count_order": None
            })

        return context


stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
class BuyItems(View):
    def get(self, request, *args, **kwargs):
        try:
            # Очищение сессии
            session_keys = tuple(request.session.keys())

            order = Order.objects.get(pk=int(session_keys[-1]))

            line_items = []
            for item_id in order.items:
                item = Item.objects.get(pk=item_id)
                
                line_items.append(
                    {
                        "price_data": {
                            "currency": item.currency,
                            "unit_amount": int(item.price) * 100 \
                                            if order.tax == None \
                                            else int(int(item.price) * 100 + ( \
                                            int(item.price) * 100 * (order.tax.percent_off / 100))),
                            "product_data": {
                                "name": item.name
                            },
                        },
                        "quantity": 1,
                    }
                )

            
            del request.session[session_keys[-1]]

            if order.discount is None:
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    success_url='http://194.36.178.183:8000/success/',
                    cancel_url='http://194.36.178.183:8000/cancel/',
                )

                return JsonResponse({'id': checkout_session.id})
            else:
                coupon = stripe.Coupon.create(percent_off=order.discount.percent_off, duration="once")
                checkout_session_with_coupon = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    discounts=[{
                        'coupon': coupon.id,
                    }],
                    success_url='http://194.36.178.183:8000/success/',
                    cancel_url='http://194.36.178.183:8000/cancel/',
                )

                return JsonResponse({'id': checkout_session_with_coupon.id})

            
        except Exception as e:
            if 'The price specified has a default currency' in str(e):
                return JsonResponse({'error': 'У товаров разные валюты'})
            print(e)

        return JsonResponse({'status': 0})


class AddToCart(View):
    def get(self, request, *args, **kwargs):
        try:
            session_keys = tuple(request.session.keys())
            session_values = tuple(request.session.values())
            print(session_keys)
            print(session_values)

            item = Item.objects.get(pk=self.kwargs["id"])
            try:
                order = Order.objects.get(pk=int(session_keys[-1]))
                order.items.append(item.id)
                order.save()

                count = int(request.session[str(order.pk)]) + 1
                request.session[order.pk] = str(count)
            except:
                order = Order(items=[item.id])
                order.save()
                request.session[str(order.pk)] = '1'
                
                

        except Exception as e:
            print(e)

        return JsonResponse({'status': 'true'})


class Success(TemplateView):
    template_name = 'success.html'


class Cancel(TemplateView):
    template_name = 'cancel.html'