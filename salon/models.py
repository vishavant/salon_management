from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branch_name
    



class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(_("email address"), unique=True)
    city = models.CharField(max_length=200) 
    is_superadmin = models.BooleanField(default=False)
    is_branch_manager = models.BooleanField(default=False)
    is_service_person = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class SuperAdmin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BranchManager(models.Model):
    bm_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ServicePerson(models.Model):
    service_person_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






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
        return self.service_name


class ServicePackage(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=200)
    services = models.ManyToManyField(Service)
    price = models.PositiveIntegerField()
    thumbanail = models.ImageField(blank=True, null=True, upload_to="service_package")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





GENDER = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
    ('Transgender', 'TRANSGENDER'),
)

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

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=15, choices=GENDER)
    service = models.ManyToManyField(Service)
    # booking_date = models.DateTimeField(help_text="Date on which customer want service")
    dob = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    booking_source = models.CharField(max_length=200, choices=BOOKING_SOURCE, blank=True, null=True)
    assigned_person = models.ForeignKey(User, on_delete=models.CASCADE)
    service_amount = models.IntegerField(blank=True, null=True)
    payment_status = models.BooleanField(default=False)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Save the Payment object first to get a primary key
        super().save(*args, **kwargs)

        # Calculate the total amount based on the selected services
        total_amount = Decimal('0.00')
        for ser in self.service.all():
            total_amount += ser.service_amount

        # Update the amount field with the calculated total
        self.amount = total_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment #{self.payment_id} - {self.client}"




    






class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


