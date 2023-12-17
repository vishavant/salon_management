from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# from .forms import CustomUserCreationForm, CustomUserChangeForm


'''
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "name", "phone", "is_superadmin", "is_branch_manager", "is_service_person","is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password", )}),
        ("Personal", {"fields": ("name", "phone", "city")}),
        ("Permissions", {"fields": ("is_superadmin", "is_branch_manager", "is_service_person", "is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
# admin.site.register(BranchManager)
# admin.site.register(SuperAdmin)
# admin.site.register(ServicePerson)
'''

#--------------------------------------------------------------------------#
# admin.py

from django.contrib import admin
from .models import Branch, ServiceCategory, Service, Booking, Product

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_id', 'branch_name', 'location', 'status', 'created_at', 'updated_at')

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'branch', 'category_name', 'description', 'created_at', 'updated_at')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'category', 'service_name', 'thumbnail', 'description', 'service_amount', 'created_at', 'updated_at')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('branch', 'name', 'phone', 'gender', 'display_services', 'service_amount', 'created_at')

    def display_services(self, obj):
        return ", ".join([service.service_name for service in obj.service.all()])

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'branch', 'product_name', 'quantity', 'created_at', 'updated_at')



