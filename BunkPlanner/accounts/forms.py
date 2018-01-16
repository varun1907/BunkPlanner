from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email


class SignUpForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Username'}),required=True)
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'First Name'}),required=True,max_length=20)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Last Name'}),required=True,max_length=20)
    email=forms.CharField(widget=forms.EmailInput(attrs={'class' : 'form-control','placeholder':'Email'}),unique=True,required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'Password'}),required=True)
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'Confirm Password'}),required=True)

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password','password2')


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            match=User.Objects.get(username=username)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("Username already exist")
    #
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if User.Objects.filter(email=email).exists():
    #         raise forms.ValidationError("email already exist")
    #     return email
    #     # except:
    #     #     return self.cleaned_data['email']
    #     # raise forms.ValidationError("email already exist")


    def clean_password2(self):
        pas=self.cleaned_data['password']
        pas2=self.cleaned_data['password2']
        MIN_LENGTH=8
        if pas and pas2:
            if pas!=pas2:
                raise forms.ValidationError("Password Not Matched")
            else:
                if len(pas)<MIN_LENGTH:
                    raise forms.ValidationError("Password Short.Minimum 8 characters long")
