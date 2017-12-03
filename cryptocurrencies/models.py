from django.db import models
from djmoney.models.fields import MoneyField


class CryptoCurrency(models.Model):
    name = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=19, decimal_places=10)
    spent = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')