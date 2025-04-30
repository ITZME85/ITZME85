from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
#django form
class Contact(forms.Form):
    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='your age')
    enquiry = forms.CharField(label='messages', widget=forms.Textarea)


#model form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email','doc','img']

# #user creation
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']
        
#Authentication
class SigninForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']