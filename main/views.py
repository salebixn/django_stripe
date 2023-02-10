import os

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Item

import stripe


#def index(request):
#    return render(request, 'index.html')


def index(request, id):
    item = Item.objects.get(pk=id)
    context = {
        "item": item,
        "STRIPE_PUBLISHABLE_KEY": os.getenv('STRIPE_PUBLISHABLE_KEY')
    }

    return render(request, 'index.html', context)


    #def get_context_data(self, **kwargs):
        #context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        #context.update({
        #        "item": item,
        #        "STRIPE_PUBLISHABLE_KEY": os.getenv('STRIPE_PUBLISHABLE_KEY')
        #    })
        #return context


stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(pk=self.kwargs["id"])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    "price_data": {
                        "currency": item.currency,
                        "unit_amount": int(item.price)*int(item.price),
                        "product_data": {
                            "name": item.name
                        },
                    },
                    "quantity": 1,
                },
            ],
            metadata={
                "product_id": item.id
            },
            mode='payment',
            success_url='http://45.95.203.39:8000/success/',
            cancel_url='http://45.95.203.39:8000/cancel/',
        )

        return JsonResponse({'id': checkout_session.id})


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')