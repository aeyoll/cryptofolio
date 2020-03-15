from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money


class CryptoCurrency(models.Model):
    name = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=19, decimal_places=10)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    spent = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')

    def total(self):
        return self.balance * self.price

    def gain(self):
        return (self.balance * self.price) - self.spent

    def gain_percentage(self):
        gain_percentage = 100
        zero = Money(0, 'EUR')

        if self.spent > zero:
            gain_percentage = self.gain() / self.spent * 100

        return gain_percentage

    def __str__(self):
        return self.name
