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
        context = {
            'crypto_currencies': crypto_currencies,
        }

        return render(request, self.template_name, context)