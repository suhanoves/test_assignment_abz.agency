from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from employees.forms import EmployeeForm
from employees.models import Employee


class CompanyStructureView(TemplateView):
    template_name = 'employees/company_structure.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        company_structure = Employee.get_annotated_list()
        context['company_structure'] = company_structure

        return context


class EmployeesView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employees/employees.html'
    paginate_by = 15
    ordering = ['surname']

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search')
        if search:
            queryset = queryset.annotate(
                search=SearchVector('name', 'patronymic', 'surname', 'position', 'salary', 'start_date'),
            ).filter(search=search)

        return queryset


class EmployeeDetailView(DetailView):
    model = Employee


class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employees:employees')


class EmployeeEdit(UpdateView):
    model = Employee
    form_class = EmployeeForm
    # fields = ('name', 'patronymic', 'surname', 'position', 'start_date', 'salary', 'photo')
    success_url = reverse_lazy('employees:employees')


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees:employees')

    # TODO переопределить логику, чтобы при удалении переназначался начальник
