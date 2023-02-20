from django import forms
import datetime
from django.core.exceptions import ValidationError
from .models import Employee,Department, Book


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields  = '__all__'
        widgets = {
            'dateBirth': forms.DateInput(attrs={'type': 'date'}),
             'gender': forms.RadioSelect,
        }
    def firstName(self):
        firstName = self.cleaned_data.get('firstName')
        if firstName == 'asd':
            raise forms.ValidationError("Name cannot be empty.")
        return firstName
    
    # Example validation error
    def clean_dateBirth(self):
        dateBirth = self.cleaned_data.get('dateBirth')
        if dateBirth and dateBirth > datetime.date.today():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return dateBirth

class DepartmentForm(forms.ModelForm):  
    class Meta:  
        model = Department  
        fields = "__all__"  

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =  "__all__"  