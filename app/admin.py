from django.contrib import admin
from .models import Payement, Entry, ExpenseType
# Register your models here

admin.site.register(Payement)
admin.site.register(Entry)
admin.site.register(ExpenseType)