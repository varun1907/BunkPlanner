from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    # email=forms.EmailField(required=True)
    username = forms.CharField(label='first_name',max_length=50,widget=forms.TextInput(
                 attrs={
                     'class' : 'form-control',
                     'placeholder':'Username'
                 }
    ))
    first_name = forms.CharField(label='first_name',max_length=50,widget=forms.TextInput(
                 attrs={
                     'class' : 'form-control',
                     'placeholder':'First Name'
                 }
    ))
    last_name = forms.CharField(label='last_name',max_length=50,widget=forms.TextInput(
                 attrs={
                     'class' : 'form-control',
                     'placeholder':'Last Name'
                 }
    ))
    email = forms.EmailField(label='email',max_length=50,widget=forms.EmailInput(
                 attrs={
                     'class' : 'form-control',
                     'placeholder':'Email'
                 }
    ))
    password1 = forms.CharField(label='password1',max_length=50,widget=forms.PasswordInput(
                 attrs={
                     'class' : 'form-control',
                     'placeholder':'Password'
                 }
    ))
    password2 = forms.CharField(label='password2',max_length=50,widget=forms.PasswordInput(
                 attrs={
                     'class' : 'form-control',
                     'placeholder':'Confirm Password'
                 }
    ))
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2')

    def save(self,commit=True):
        user=super(SignUpForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()

        return user
