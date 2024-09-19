from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('approve_expenses/', views.approve_expenses, name='approve_expenses'),
    path('company_account/', views.company_account, name='company_account'),
    path('submit_expenses/', views.submit_expenses, name='submit_expenses'),
    path('manage_income/', views.manage_income, name='manage_income'),
    path('report/', views.report, name='report'),
]
