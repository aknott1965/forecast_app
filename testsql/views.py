# views.py

from django.shortcuts import render
from .utils import import_sales_data

def import_data_view(request):
    import_sales_data()
    return render(request, 'import_complete.html')

