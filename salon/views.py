from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import BranchForm, BookingForm, ProductForm, EmployeeForm, SearchForm
from django.db.models import Sum
# Create your views here.


def index(request):
    return render(request, "home/index.html")




# def users(request):
#     return render(request, "admin/users.html")

# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'accounts/user_list.html', {'users': users})

# def user_detail(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     return render(request, 'accounts/user_detail.html', {'user': user})

# def user_create(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('salon:user_list')
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'accounts/user_form.html', {'form': form, 'action': 'Create'})

# def user_update(request, user_id):
#     user = get_object_or_404(User, pk=user_id)

#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('salon:user_list')
#     else:
#         form = CustomUserCreationForm(instance=user)

#     return render(request, 'accounts/user_form.html', {'form': form, 'action': 'Update'})

# def user_delete(request, user_id):
#     user = get_object_or_404(User, pk=user_id)

#     if request.method == 'POST':
#         user.delete()
#         return redirect('salon:user_list')

#     return render(request, 'accounts/user_confirm_delete.html', {'user': user})





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
    bookings = Booking.objects.all().order_by('-created_at')
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
    payments = Booking.objects.all().order_by('-created_at')
    return render(request, "reports/payments/payment_list.html", {'payments':payments})



def profile(request):
    return render(request, "accounts/profile.html")




def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salon:product_list')
    else:
        form = ProductForm()

    return render(request, 'products/product_form.html', {'form': form, 'action': 'Add'})

def product_update(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('salon:product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/product_form.html', {'form': form, 'action': 'Update'})

def product_delete(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('salon:product_list')

    return render(request, 'products/product_confirm_delete.html', {'product': product})




#-------------------------------------------------------------------

# Creating Account Views

# salon/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('salon:login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('salon:home')  # Replace 'home' with your desired home page URL
        else:
            messages.error(request, 'Login failed. Please check your username and password.')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('salon:login')





def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'employee/employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully.')
            return redirect('salon:employee_list')
        else:
            messages.error(request, 'Error creating employee. Please correct the errors below.')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form, 'action': 'Create'})

def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('salon:employee_list')
        else:
            messages.error(request, 'Error updating employee. Please correct the errors below.')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_update.html', {'form': form, 'action': 'Update'})

def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('salon:employee_list')
    return render(request, 'employee/employee_delete.html', {'employee': employee})
    




# views.py

from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
import xhtml2pdf.pisa as pisa
from .models import Booking

class InvoicePDFView(View):
    def get(self, request, booking_id, *args, **kwargs):
        booking = Booking.objects.get(pk=booking_id)
        template_path = 'bookings/invoice.html'  # Replace with the actual path to your template

        # Load the template
        template = get_template(template_path)
        context = {'booking': booking}

        # Render the template
        html = template.render(context)
        
        # Create PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="invoice_{booking.booking_id}.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)

        # Check if PDF creation was successful
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        return response


class InvoicePreviewView(View):
    def get(self, request, booking_id, *args, **kwargs):
        booking = Booking.objects.get(pk=booking_id)
        pdf_url = reverse_lazy('salon:invoice_pdf', kwargs={'booking_id': booking.pk})
        context = {'pdf_url': pdf_url}
        return render(request, 'branch/invoice_pdf_preview.html', context)
    


from datetime import date

def admin_dashboard(request):
    # Total bookings
    today = date.today()
    total_bookings_today = Booking.objects.filter(created_at__date=today).count()

    # Total branches
    total_branches = Branch.objects.count()

    # Total sum of payments recorded
    total_payments_today = Booking.objects.filter(created_at__date=today, payment_status=True).aggregate(Sum('service_amount'))['service_amount__sum'] or 0

    # Total employees
    total_employees = Employee.objects.count()
    
    today = date.today()
    today_bookings = Booking.objects.filter(created_at__date=today).order_by('-created_at')
    context = {
        'total_bookings_today': total_bookings_today,
        'total_branches': total_branches,
        'total_payments_today': total_payments_today,
        'total_employees': total_employees,
        'today_bookings': today_bookings
    }
    return render(request, 'admin/dashboard.html', context)



def search_results(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        # Perform your search logic here
        results = Booking.objects.filter(name__icontains=query)  # Update with your search fields

    context = {'form': form, 'results': results}
    return render(request, 'bookings/search_results.html', context)