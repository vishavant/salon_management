from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, ServicePerson, BranchManager, SuperAdmin, Branch, Service, ServiceCategory, Booking, ServicePackage

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


class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['branch', 'category_name', 'description']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['branch', 'category', 'service_name', 'thumbnail', 'description', 'service_amount']

    def __init__(self, branch, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = ServiceCategory.objects.filter(branch=branch)




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