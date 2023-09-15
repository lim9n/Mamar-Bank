from django.contrib import admin

from .models import UserAddress,UserBankAccount

admin.site.register(UserBankAccount)

admin.site.register(UserAddress)
