# views.py

from django.shortcuts import render
from .utils import import_sales_data
from .models import ActualSales

def import_data_view(request):
    import_sales_data()
    data = ActualSales.objects.all()
    return render(request, 'import_complete.html',{'data': data} )

