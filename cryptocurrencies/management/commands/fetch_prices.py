from django.core.management.base import BaseCommand, CommandError
from cryptocurrencies.models import CryptoCurrency
from requests.exceptions import RequestException
import requests


class Command(BaseCommand):
    help = 'Fetch prices from coinmarketcap'

    def handle(self, *args, **options):
        crypto_currencies = CryptoCurrency.objects.all()
        coinbase_api = 'https://api.coinmarketcap.com/v1/ticker/%s/?convert=EUR'

        for crypto_currency in crypto_currencies:
            try:
                results = requests.get(coinbase_api % crypto_currency.name)
                results_json = results.json()
                price = results_json[0]['price_eur']
                crypto_currency.price = price
                crypto_currency.save()
                self.stdout.write(self.style.SUCCESS('Successfully fetch price for "%s"' % crypto_currency.name))
            except RequestException:
                raise CommandError('Poll "%s" does not exist' % poll_id)
