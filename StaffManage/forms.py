__author__ = '9'

from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Row, Div, Field, Submit, Layout, HTML, Hidden, Button
from crispy_forms.bootstrap import TabHolder, Tab, FormActions, InlineRadios

class StaffManageForm(forms.Form):
    sm_name = forms.CharField(
        label='name:',
        required=False,
    )

    sm_sex = forms.CharField(
        label='sex:',
        required=False,
    )
    sm_type = forms.CharField(
        label='type',
        required=False,
    )


    def __init__(self, *args, **kwargs):
        super(StaffManageForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Row(
                Div('sm_name', css_class='col-md-4'),
                Div('sm_sex', css_class='col-md-4'),
                Div('sm_type', css_class='col-md-4'),
            ),

            HTML('''<hr>'''),

            Row(
                FormActions(
                    Submit('save', 'Query'),
                    Button('add', 'Add', css_id='addItem'),
                    # hidden=True,
                )
            )
        )

class AddItemForm(forms.Form):
    sm_name = forms.CharField(
        label='name:',
        required=True,
    )

    sm_sex = forms.CharField(
        label='sex:',
        required=True,
    )
    sm_type = forms.CharField(
        label='type',
        required=True,
    )


    def __init__(self, *args, **kwargs):
        super(AddItemForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-verical'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Div('sm_name', css_class='col-md-4'),
            Div('sm_sex', css_class='col-md-4'),
            Div('sm_type', css_class='col-md-4'),

            FormActions(
                Button('cancel', 'Cancel'),
                Button('ok', 'Ok', css_id='add_item11'),
                # hidden=True,
            )
        )