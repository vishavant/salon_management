from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import BranchForm, BookingForm, CustomUserCreationForm
# Create your views here.


def index(request):
    return render(request, "home/index.html")


def admin_dashboard(request):
    return render(request, "admin/dashboard.html")


def users(request):
    return render(request, "admin/users.html")

def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'accounts/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salon:user_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/user_form.html', {'form': form, 'action': 'Create'})

def user_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('salon:user_list')
    else:
        form = CustomUserCreationForm(instance=user)

    return render(request, 'accounts/user_form.html', {'form': form, 'action': 'Update'})

def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('salon:user_list')

    return render(request, 'accounts/user_confirm_delete.html', {'user': user})





def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branch/branch_list.html', {'branches': branches})

def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    return render(request, 'branch/branch_detail.html', {'branch': branch})

def branch_create(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salon:branch_list')
    else:
        form = BranchForm()

    return render(request, 'branch/branch_form.html', {'form': form, 'action': 'Create'})

def branch_update(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)

    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('salon:branch_list')
    else:
        form = BranchForm(instance=branch)

    return render(request, 'branch/branch_form.html', {'form': form, 'action': 'Update'})

def branch_delete(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    
    if request.method == 'POST':
        branch.delete()
        return redirect('salon:branch_list')

    return render(request, 'branch/branch_confirm_delete.html', {'branch': branch})




from .forms import ServiceCategoryForm

def service_category_list(request):
    categories = ServiceCategory.objects.all()
    return render(request, 'services/service_category_list.html', {'categories': categories})

def service_category_detail(request, cat_id):
    category = get_object_or_404(ServiceCategory, pk=cat_id)
    return render(request, 'services/service_category_detail.html', {'category': category})

def service_category_create(request):
    if request.method == 'POST':
        form = ServiceCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salon:service_category_list')
    else:
        form = ServiceCategoryForm()

    return render(request, 'services/service_category_form.html', {'form': form, 'action': 'Create'})

def service_category_update(request, cat_id):
    category = get_object_or_404(ServiceCategory, pk=cat_id)

    if request.method == 'POST':
        form = ServiceCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('salon:service_category_list')
    else:
        form = ServiceCategoryForm(instance=category)

    return render(request, 'services/service_category_form.html', {'form': form, 'action': 'Update'})

def service_category_delete(request, cat_id):
    category = get_object_or_404(ServiceCategory, pk=cat_id)
    
    if request.method == 'POST':
        category.delete()
        return redirect('salon:service_category_list')

    return render(request, 'services/service_category_confirm_delete.html', {'category': category})




from .forms import ServiceForm

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'services/service_detail.html', {'service': service})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('salon:service_list')
    else:
        form = ServiceForm()

    return render(request, 'services/service_form.html', {'form': form, 'action': 'Create'})

def service_update(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('salon:service_list')
    else:
        form = ServiceForm(instance=service)

    return render(request, 'services/service_form.html', {'form': form, 'action': 'Update'})

def service_delete(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    
    if request.method == 'POST':
        service.delete()
        return redirect('salon:service_list')

    return render(request, 'services/service_confirm_delete.html', {'service': service})


from .forms import ServicePackageForm

def service_package_list(request):
    service_packages = ServicePackage.objects.all()
    return render(request, 'services/service_package_list.html', {'service_packages': service_packages})

def service_package_detail(request, package_id):
    service_package = get_object_or_404(ServicePackage, pk=package_id)
    return render(request, 'services/service_package_detail.html', {'service_package': service_package})

def service_package_create(request):
    if request.method == 'POST':
        form = ServicePackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('salon:service_package_list')
    else:
        form = ServicePackageForm()

    return render(request, 'services/service_package_form.html', {'form': form, 'action': 'Create'})

def service_package_update(request, package_id):
    service_package = get_object_or_404(ServicePackage, pk=package_id)

    if request.method == 'POST':
        form = ServicePackageForm(request.POST, request.FILES, instance=service_package)
        if form.is_valid():
            form.save()
            return redirect('salon:service_package_list')
    else:
        form = ServicePackageForm(instance=service_package)

    return render(request, 'services/service_package_form.html', {'form': form, 'action': 'Update'})

def service_package_delete(request, package_id):
    service_package = get_object_or_404(ServicePackage, pk=package_id)

    if request.method == 'POST':
        service_package.delete()
        return redirect('salon:service_package_list')

    return render(request, 'services/service_package_confirm_delete.html', {'service_package': service_package})





def record_payment(request):
    pass


def generate_invoice(request):
    pass



def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salon:booking_list')
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {'form': form, 'action': 'Create'})

def booking_update(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('salon:booking_list')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'bookings/booking_form.html', {'form': form, 'action': 'Update'})

def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == 'POST':
        booking.delete()
        return redirect('salon:booking_list')

    return render(request, 'bookings/booking_confirm_delete.html', {'booking': booking})


def display_payments(request):
    return render(request, "payments/payment_list.html")



def profile(request):
    return render(request, "accounts/profile.html")