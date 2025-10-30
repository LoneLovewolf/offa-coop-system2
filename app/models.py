from django.db import models
from django.contrib.auth.models import User

class Cooperative(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(null=True)
    
    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(null=True)
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('contribution', 'Contribution'),
        ('loan', 'Loan Issued'),
        ('expense', 'Expense'),
        ('repayment', 'Loan Repayment'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"

class Loan(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('repaid', 'Repaid'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan {self.amount} ({self.status})"
