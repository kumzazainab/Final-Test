from django.shortcuts import render, redirect
from .models import Company, Account, Expenses, Report, Income
from django.contrib.auth.views import LoginView
from .forms import LoginForm, ExpensesForm, IncomeForm
from django.contrib.auth.mixins import LoginRequiredMixin

def company_account(request):
    accounts = request.user.company.accounts_set.all()
    return redirect(request,'accounts/company_account.html', {'accounts': accounts})

def home(request):
    return render(request, 'accounts/home.html')

def manage_income(request, pk):
    accounts = Account.objects.get(pk=pk)
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save()
            income.accounts = accounts
            income.save()
            return render(request, 'accounts/manage_income.html')
    else:
        form = IncomeForm()
    return render(request, 'accounts/manage_income.html', {'form': form})

def submit_expenses(request):
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_account')
    else:
        form = ExpensesForm()
    return redirect(request, 'accounts/submit_expenses.html', {'form': form})

def approve_expenses(request, pk):
    expenses = Expenses.object.get(pk=pk)
    expenses.approved = True
    expenses.save()
    return redirect(request, 'accounts/approve_expenses.html', {'expenses': expenses})

def report(request):
    if request.user.role == 'website_owner':
        report = Report.objects.all()
    elif request.user.role == 'company_owner':
        report = Report.objects.filter(company=request.user.company)
    else:
        return redirect('unauthorized')
    return render(request, 'accounts/report.html', {'report': report})


class CustomLoginView(LoginView, LoginRequiredMixin):
    form_class = LoginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)