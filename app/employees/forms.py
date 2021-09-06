from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div
from treebeard.forms import MoveNodeForm

from employees.models import Employee


# EmployeeForm = movenodeform_factory(Employee)

class EmployeeForm(MoveNodeForm):
    class Meta:
        model = Employee
        exclude = ('depth', 'numchild', 'path')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Fieldset(
                'first arg is the legend of the fieldset',

                FloatingField('surname'),
                Div(
                    Div(FloatingField('name'), css_class='flex-fill pe-2'),
                    Div(FloatingField('patronymic'), css_class='flex-fill ps-2'),
                    css_class='d-flex mb-4',
                ),
                FloatingField('position'),
                Div(
                    Div(FloatingField('start_date'), css_class='flex-fill pe-2'),
                    Div(FloatingField('salary'), css_class='flex-fill ps-2'),
                    css_class='d-flex justify-content-between flex-fill'
                ),
                Div(
                    Div(FloatingField('_position'), css_class='flex-shrink pe-2'),
                    Div(FloatingField('_ref_node_id'), css_class='flex-fill ps-2'),
                    css_class='d-flex justify-content-between'
                ),
            ),
            # ButtonHolder(
            #     Submit('submit', 'Save employee', css_class='button white')
            # )
        )
        self.helper.add_input(Submit('submit', 'Save employee'))
