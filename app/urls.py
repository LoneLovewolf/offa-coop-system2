from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('cooperative-create/', views.create_cooperative, name='cooperative_create'),
    path('income-create/', views.create_income, name='income_create'),
    path('expense-create/', views.create_expense, name='expense_create'),
    path('transaction-create/', views.create_transaction, name='transaction_create'),
    path('loan-request/', views.request_loan, name='loan_request'),
    path('generate-report/', views.generate_report, name='generate_report'),
]
