from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from .models import CryptoCurrency


@method_decorator(login_required, name='get')
class IndexView(View):
    template_name = 'cryptocurrencies/index.html'

    def get(self, request, *args, **kwargs):
        crypto_currencies = CryptoCurrency.objects.all()
        total_spent = 0
        total_gain = 0
        total = 0


        for crypto_currency in crypto_currencies:
            total_spent += crypto_currency.spent
            total_gain += crypto_currency.gain()
            total += crypto_currency.total()


        context = {
            'crypto_currencies': crypto_currencies,
            'total_spent': total_spent,
            'total_gain': total_gain,
            'total': total,
        }

        return render(request, self.template_name, context)
