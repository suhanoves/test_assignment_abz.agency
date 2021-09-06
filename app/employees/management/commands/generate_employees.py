import itertools
import json
import random
from pathlib import Path

from django.core.management import BaseCommand, CommandError
from mimesis import Generic
from mimesis.builtins import RussiaSpecProvider
from mimesis.enums import Gender

from employees.management.commands.data import POSITIONS, SALARIES
from employees.models import Employee


class Command(BaseCommand):
    model = "employees.employee"
    pk = itertools.count(start=1)
    adder = 0

    generic = Generic(locale='ru')
    generic_ru = RussiaSpecProvider()

    help = 'Generates an arbitrary number of employees with a five-level hierarchy'

    def add_arguments(self, parser):
        parser.add_argument(
            'number', nargs='?', default=1000, type=int,
            help='number of generated users'
        )

    def __init__(self):
        super().__init__()
        self.employees = []

    @staticmethod
    def get_path_suffix(num):
        numconv_obj = Employee.numconv_obj()
        return numconv_obj.int2str(num).zfill(4)

    @classmethod
    def create_employee(cls, *, path_prefix='', lvl, num, numchild):
        gender = random.choice(list(Gender))

        model = cls.model
        pk = next(cls.pk)
        path = f"{path_prefix}{cls.get_path_suffix(num)}"
        name = cls.generic.person.name(gender=gender)
        patronymic = cls.generic_ru.patronymic(gender=gender)
        surname = cls.generic.person.surname(gender=gender)
        position = random.choice(POSITIONS[lvl])
        start_date = str(cls.generic.datetime.date(start=2000, end=2021))
        salary = f"{random.choice(SALARIES[lvl])}.00"
        photo = str(Path(f"/photos/{gender.value}/{str(random.randint(1, 20)).zfill(2)}.jpg"))

        employee = {"model": model,
                    "pk": pk,
                    "fields": {"path": path,
                               "depth": lvl,
                               "numchild": numchild,
                               "name": name,
                               "patronymic": patronymic,
                               "surname": surname,
                               "position": position,
                               "start_date": start_date,
                               "salary": salary,
                               "photo": photo
                               },
                    }

        return employee

    def add_employee(self, path_prefix, lvl, num, numchild):
        employee = self.create_employee(path_prefix=path_prefix, lvl=lvl, num=num, numchild=numchild)
        self.adder += 1
        self.employees.append(employee)
        return employee['fields']['path']

    def get_employees(self):
        employee_lvl_1 = self.create_employee(lvl=1, num=1, numchild=8)
        self.adder += 1
        self.employees.append(employee_lvl_1)
        path_prefix_lvl_1 = employee_lvl_1['fields']['path']

        for a in range(1, 9):
            numchild_lvl_2 = random.randint(6, 18)
            path_prefix_lvl_2 = self.add_employee(path_prefix=path_prefix_lvl_1, lvl=2,
                                                  num=a, numchild=numchild_lvl_2)

            for b in range(1, numchild_lvl_2 + 1):
                numchild_lvl_3 = random.randint(8, 24)
                path_prefix_lvl_3 = self.add_employee(path_prefix=path_prefix_lvl_2, lvl=3,
                                                      num=b, numchild=numchild_lvl_3)

                for c in range(1, numchild_lvl_3 + 1):
                    numchild_lvl_4 = random.randint(20, 44)
                    path_prefix_lvl_4 = self.add_employee(path_prefix=path_prefix_lvl_3, lvl=4,
                                                          num=c, numchild=numchild_lvl_4)
                    for d in range(1, numchild_lvl_4 + 1):
                        self.add_employee(path_prefix=path_prefix_lvl_4, lvl=5, num=d, numchild=0)

        with open('fixtures/data.json', 'w') as outfile:
            json.dump(self.employees, outfile, ensure_ascii=False)

    def handle(self, *args, **options):
        number = options['number']

        # TODO доделать генерацию по принимаемому количеству пользователей
        if number < 1:
            raise CommandError('Количество генерируемых сотрудников должно быть больше 0')

        self.get_employees()
        self.stdout.write(self.style.SUCCESS(f'Successfully create employee'))
