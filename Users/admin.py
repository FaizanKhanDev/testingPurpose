from django.contrib import admin
from django.contrib.admin import ModelAdmin
from Users.models import Trader, User, Order


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ['symbol', 'trader_name',
                    'side', 'is_active']


@admin.register(Trader)
class TraderAdmin(ModelAdmin):
    list_display = ['user_name', 'admin', 'link']


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ['username', 'first_name', ]
