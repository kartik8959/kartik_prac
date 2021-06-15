from django import forms
from django.contrib.auth.models import User
import re
from home.utils import prepareCityList
from .models import Institutes,City
from django.contrib.auth.forms import AuthenticationForm
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','password')
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',"maxlength":"12"}))
    contact_no=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    
    def clean_username(self):
        uname=self.cleaned_data['username']
        if not re.search("^[a-zA-Z\d@_]{5,20}$",uname):
            raise forms.ValidationError("Invalid User Name")
        print(uname)
        return uname

    def clean_email(self):
        email=self.cleaned_data['email']
        if not re.search('^([a-zA-Z\d\._]+)@([a-zA-Z\d]{2,})\.([a-zA-Z\d]{2,5})(\.[A-Za-z]{2,5})?$',email):
                raise forms.ValidationError("Invalid Email id")
        return email   

    def clean_password(self):
        pwd=self.cleaned_data['password']
        if not re.search("^[a-zA-Z\d@]{6,20}$",pwd):
            raise forms.ValidationError("you typed invalid password ")
        return pwd

    def clean_contact_no(self):
        phone=self.cleaned_data['contact_no']
        if not re.search("^[5-9][\d]{9}$",phone):
           raise forms.ValidationError("invalid contact number")
        return phone
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.forms.widgets import NumberInput, Select, TextInput, Textarea

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':"form-control"}))
    password=forms.CharField(label=_("password"),strip="false",widget=forms.PasswordInput(attrs={"autocomplete":'current_password','class':'form-control'}))


class profile_form(forms.ModelForm):
    class Meta:
            model=Institutes
            fields=['name','details','start_date','address','city','contact',"start_date"]
    
    name=forms.CharField(widget=TextInput(attrs={"class":"form-control","rows":"5"}))
    details=forms.CharField(widget=Textarea(attrs={"class":"form-control","rows":"5"}))
    address=forms.CharField(widget=Textarea(attrs={"class":"form-control","rows":"3","cols":"56"}))
    contact=forms.IntegerField(widget=NumberInput(attrs={"class":"form-control"}))
    cities=prepareCityList()

    city=forms.ChoiceField(widget=Select(attrs={"class":"form-control"}),choices=cities)
    start_date=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control",'type':"date"}))

    def clean_city(self):
        city_id=self.cleaned_data['city']
        return City(id=city_id)


