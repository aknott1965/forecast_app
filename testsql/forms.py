from django import forms
from .models import ActualSales

class MyFilterForm(forms.Form):
    field1_filter = forms.CharField(label='Field 1 Filter', required=False)
    field2_filter = forms.CharField(label='Field 2 Filter', required=False)
    # Add more fields as needed for additional filters

class MyModelForm(forms.ModelForm):
    class Meta:
        model = ActualSales
        fields = ['Sales_person', 'Cust_no']  # Specify the fields you want to include in the form

# class MyFilterForm(forms.Form):
#     CATEGORY_CHOICES = [
#         ('category1', 'Category 1'),
#         ('category2', 'Category 2'),
#         # Add more choices as needed
#     ]
#     category_filter = forms.ChoiceField(label='Category', choices=CATEGORY_CHOICES, required=False)
