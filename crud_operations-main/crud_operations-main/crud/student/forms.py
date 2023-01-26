from django import forms  
from student.models import student
from django.forms import fields

class StudentForm(forms.ModelForm):  
    class Meta:  
        model = student  
        fields = "__all__"  