from django.db import models

# Create your models here.

class ActualSales(models.Model):
    # Define fields that match the columns in your SQL Server table
    Sales_person = models.CharField(max_length=100)
    Cust_no = models.CharField(max_length=100)
    Sales_Amount = models.IntegerField()
    # Add more fields as needed

