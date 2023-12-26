from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    branch_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branch_name


GENDER = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
    ('Transgender', 'TRANSGENDER'),
)   

class Employee(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=100, choices=GENDER)
    address = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class ServiceCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name



class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    # branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='service_imaege', null=True, blank=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    service_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_name} - Rs.{self.service_amount}"


class ServicePackage(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=200)
    services = models.ManyToManyField(Service)
    price = models.PositiveIntegerField()
    thumbanail = models.ImageField(blank=True, null=True, upload_to="service_package")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







BOOKING_SOURCE = (
    ('Google', 'GOOGLE'),
    ('Instagram', 'INSTAGRAM'),
    ('Website', 'WEBSITE'),
    ('Refferal', 'REFFERAL'),
)

PAYMENT_MODE = (
    ('CASH', 'Cash'),
    ('ONLINE', 'Online'),
)

PAYMENT_STATUS = (
    ('PENDING', 'Pending'),
    ('RECEIVED', 'Received'),
)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=15, choices=GENDER)
    services = models.ManyToManyField(Service)
    # booking_date = models.DateTimeField(help_text="Date on which customer want service")
    dob = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    booking_source = models.CharField(max_length=200, choices=BOOKING_SOURCE, blank=True, null=True)
    assigned_person = models.ForeignKey(Employee, on_delete=models.CASCADE)
    service_amount = models.IntegerField(blank=True, null=True)
    payment_status = models.BooleanField(default=False)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def calculate_total_service_amount(self):
        """
        Calculate the total service amount for the booking.
        """
        total_amount = self.services.aggregate(Sum('service_amount'))['service_amount__sum']
        return total_amount or 0




class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


