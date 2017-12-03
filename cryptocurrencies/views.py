from django.template import loader
from django.http import HttpResponse
from .models import CryptoCurrency


def index(request):
    crypto_currencies = CryptoCurrency.objects.all()
    template = loader.get_template('cryptocurrencies/index.html')
    context = {
        'crypto_currencies': crypto_currencies,
    }
    return HttpResponse(template.render(context, request))