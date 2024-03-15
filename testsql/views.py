# views.py

from django.shortcuts import render
from .utils import import_sales_data
from .models import ActualSales
from .forms import MyFilterForm, MyModelForm

def import_data_view(request):
    import_sales_data()
    data = ActualSales.objects.all()
    return render(request, 'raw_data.html',{'data': data} )

def filtered_data_view(request):
    import_sales_data()
    
    if request.method == 'GET':
        form = MyModelForm(request.GET)  # Bind form data to request.GET
        queryset = ActualSales.objects.all()  # Initial queryset

        if form.is_valid():
            # Retrieve form data
            field1_filter = form.cleaned_data.get('field1_filter')
            field2_filter = form.cleaned_data.get('field2_filter')
            # Add more fields as needed

            # Apply filters to the queryset
            
            if field1_filter:
                queryset = queryset.filter(Sales_person__icontains=field1_filter)
            if field2_filter:
                queryset = queryset.filter(Cust_no__icontains=field2_filter)
            # Add more filters as needed

            # Pass the filtered data to the template
            

        else:
            form = MyModelForm()  # Create an empty form

        return render(request, 'filtered_data.html', {'form': form, 'filtered_data': queryset})

