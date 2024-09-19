from django.contrib import admin
from .models import Company, Income, Account, Expenses, Report

# Register your models here.
admin.site.register(Company)
admin.site.register(Income)
admin.site.register(Account)
admin.site.register(Expenses)
admin.site.register(Report)