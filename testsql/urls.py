# urls.py

from django.urls import path
from .views import import_data_view, filtered_data_view

urlpatterns = [
    # Define the URL pattern for the import data view
    path('filtered-data/', filtered_data_view, name='filtered_data'),
    path('raw-data/', import_data_view, name = 'import_data')
    
    # Add other URL patterns as needed
]
