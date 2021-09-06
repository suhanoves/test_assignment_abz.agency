from django.urls import path

from employees.views import *

app_name = 'employees'

urlpatterns = [
    path('company_structure/', CompanyStructureView.as_view(), name='company_structure'),
    path('employees/', EmployeesView.as_view(), name='employees'),
    path('employee:<int:pk>', EmployeeDetailView.as_view(), name='employee_detail'),
    path('create/', EmployeeCreate.as_view(), name='employee_create'),
    path('edit/<int:pk>', EmployeeEdit.as_view(), name='employee_edit'),
    path('delete/<int:pk>', EmployeeDelete.as_view(), name='employee_delete'),
]
