from django import forms
from .models import student
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

'''class student_form(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__' '''

class student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = ['id', 'name', 'email', 'password']
        widget = {
            'name' : forms.TextInput(),
            'email': forms.EmailField(),
            'password': forms.PasswordInput()
        }
