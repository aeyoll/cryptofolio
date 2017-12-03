from django.contrib import admin
from .models import CryptoCurrency


class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'balance', 'spent')


admin.site.register(CryptoCurrency, CryptoCurrencyAdmin)