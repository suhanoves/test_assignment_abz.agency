from django.urls import path
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from employees.views import *

app_name = 'employees'

urlpatterns = [
    path('employees/', EmployeesView.as_view(), name='employees'),
    path('company_structure/', CompanyStructureView.as_view(), name='company_structure'),
    path('', RedirectView.as_view(url=reverse_lazy('employees:employees'), permanent=True)),
]
