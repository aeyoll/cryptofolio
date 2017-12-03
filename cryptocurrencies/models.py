from django.db import models
from djmoney.models.fields import MoneyField


class CryptoCurrency(models.Model):
    name = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=19, decimal_places=10)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    spent = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')

    def total(self):
        return self.balance * self.price


    def gain(self):
        return (self.balance * self.price) - self.spent


    def __str__(self):
        return self.name