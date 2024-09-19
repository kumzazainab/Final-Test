from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 100)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

class Income(models.Model):
    account = models.ForeignKey
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Account(models.Model):
    Name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    income = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    expenses = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

class Expenses(models.Model):
    user = models.CharField(max_length=100)
    account = models.CharField(max_length= 100)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    approved = models.BooleanField

class Report(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)