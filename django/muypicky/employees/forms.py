from .models import EmployeeModel

from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ['name', 'address', 'dob', 'phone', 'emp_id']
