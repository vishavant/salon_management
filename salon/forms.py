from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Employee, Branch, Service, ServiceCategory, Booking, ServicePackage, Product
from django.forms import BaseInlineFormSet

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
#-----------------------------------------------------------------------

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['user','branch_name', 'location', 'status']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'branch_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={}),
        }


class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['branch', 'category_name', 'description']

        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'service_name', 'thumbnail', 'service_amount', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'service_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'service_name': forms.TextInput(attrs={'class': 'form-control'}),
        }




class ServicePackageForm(forms.ModelForm):
    class Meta:
        model = ServicePackage
        fields = ['package_name', 'services', 'price', 'thumbanail']

        widgets = {
            'package_name': forms.TextInput(attrs={'class': 'form-control'}),
            'services': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['branch', 'name', 'phone', 'gender', 'services', 'dob', 'location', 'booking_source', 'assigned_person', 'service_amount', 'payment_mode', 'payment_status','remark']
        
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'services': forms.CheckboxSelectMultiple(attrs={}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'booking_source': forms.Select(attrs={'class': 'form-control'}),
            'assigned_person': forms.Select(attrs={'class': 'form-control'}),
            'service_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control'}),
            'payment_status': forms.CheckboxInput(attrs={}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }







class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['branch', 'product_name', 'quantity']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }





class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['branch', 'name', 'phone', 'gender', 'address', 'status']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            # 'status': forms.CheckboxInput(attrs={}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')





class BookingForma(forms.ModelForm):
    # ...
    service_amount = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Booking
        fields = ['branch', 'name', 'phone', 'gender', 'services', 'dob', 'location', 'booking_source', 'assigned_person', 'service_amount', 'payment_mode', 'payment_status', 'remark']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'services': forms.CheckboxSelectMultiple(),
            'service_amount': forms.HiddenInput(),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'booking_source': forms.Select(attrs={'class': 'form-control'}),
            'assigned_person': forms.Select(attrs={'class': 'form-control'}),
            
            'payment_mode': forms.Select(attrs={'class': 'form-control'}),
            'payment_status': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }
