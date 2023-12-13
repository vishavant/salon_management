from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Payment, User, Branch, Service, ServiceCategory, Booking, ServicePackage, Product

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("name", "phone", "email", "city")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("name", "phone", "email", "city")


# from django.db import transaction


# class ServiceSignUpForm(UserCreationForm):
#     interests = forms.ModelMultipleChoiceField(
#         queryset=ServicePerson.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True
#     )

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_student = True
#         user.save()
#         student = Student.objects.create(user=user)
#         student.interests.add(*self.cleaned_data.get('interests'))
#         return user


#-----------------------------------------------------------------------

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['branch_name', 'location', 'status']
        widgets = {
            'branch_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['branch', 'category_name', 'description']


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



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['branch', 'name', 'phone', 'gender', 'service', 'dob', 'location', 'booking_source', 'assigned_person', 'service_amount', 'remark']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'booking_source': forms.TextInput(attrs={'class': 'form-control'}),
            'assigned_person': forms.Select(attrs={'class': 'form-control'}),
            'service_amount': forms.TextInput(attrs={'class': 'form-control'}),
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



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['client', 'services', 'assigned_person', 'payment_mode', 'amount']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'services': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'assigned_person': forms.Select(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

