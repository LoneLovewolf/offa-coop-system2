from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from datetime import datetime
from .forms import CooperativeForm, IncomeForm, ExpenseForm, TransactionForm, LoanForm
from .models import Cooperative, Income, Expense, Transaction, Loan

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'app/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'app/register.html')

@login_required
def home(request):
    cooperatives = Cooperative.objects.filter(user=request.user)
    total_income = Income.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    total_balance = total_income - total_expense
    context = {'cooperatives': cooperatives, 'total_balance': total_balance}
    return render(request, 'app/home.html', context)

@login_required
def create_cooperative(request):
    if request.method == 'POST':
        form = CooperativeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
    form = CooperativeForm()
    return render(request, 'app/cooperative_create.html', {'form': form})

@login_required
def create_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.cooperative = Cooperative.objects.first()
            obj.save()
            return redirect('home')
    form = IncomeForm()
    return render(request, 'app/income_create.html', {'form': form})

@login_required
def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.cooperative = Cooperative.objects.first()
            obj.save()
            return redirect('home')
    form = ExpenseForm()
    return render(request, 'app/expense_create.html', {'form': form})

@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.cooperative = Cooperative.objects.first()
            obj.save()
            return redirect('home')
    form = TransactionForm()
    return render(request, 'app/transaction_create.html', {'form': form})

@login_required
def request_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.cooperative = Cooperative.objects.first()
            member_contributions = 50000  # Replace with actual logic
            if member_contributions >= 50000 and obj.amount <= (member_contributions * 0.5):
                obj.status = 'approved'
            else:
                obj.status = 'rejected'
            obj.save()
            return redirect('home')
    form = LoanForm()
    return render(request, 'app/loan_request.html', {'form': form})

@login_required
def generate_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="financial_report.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 800, "Offa Market Financial Report")
    p.drawString(100, 780, f"Date: {datetime.now()}")
    transactions = Transaction.objects.filter(user=request.user)
    y = 760
    for tx in transactions:
        p.drawString(100, y, f"{tx.date}: {tx.type} - {tx.amount}")
        y -= 20
    p.save()
    return response
