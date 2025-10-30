from django import forms
from .models import Cooperative, Income, Expense, Transaction, Loan

class CooperativeForm(forms.ModelForm):
    class Meta:
        model = Cooperative
        fields = ['name']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['name', 'amount', 'date']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'description']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['amount']
