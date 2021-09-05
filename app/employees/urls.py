from django.urls import path

from employees.views import *

app_name = 'employees'

urlpatterns = [
    path('company_structure/', CompanyStructureView.as_view(), name='company_structure'),
    path('employees/', EmployeesView.as_view(), name='employees'),
]
