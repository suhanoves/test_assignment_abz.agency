from django.db import models
from django.urls import reverse
from treebeard.mp_tree import MP_Node


def employees_photo_directory_path(instance, filename):
    """Generate path to user photo."""
    return f'employees_photos/{filename}'


class Employee(MP_Node):
    name = models.CharField(max_length=200, null=False, blank=False)
    patronymic = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=False, blank=False, db_index=True)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    salary = models.DecimalField(max_digits=19, decimal_places=2)
    photo = models.ImageField(upload_to=employees_photo_directory_path, null=True, blank=True)

    node_order_by = ['surname']

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def get_fullname_ru(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def get_absolute_url(self):
        return reverse('employees:employee_detail', kwargs={'pk': self.pk})
