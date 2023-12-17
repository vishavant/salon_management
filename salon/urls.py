from django.urls import path
from salon import views

app_name = 'salon'

urlpatterns = [
    path('index', views.index),
    path('', views.admin_dashboard, name='home'),
    # path('users', views.users, name='users'),

    path('branches/', views.branch_list, name='branch_list'),
    path('branches/<int:branch_id>/', views.branch_detail, name='branch_detail'),
    path('branches/create/', views.branch_create, name='branch_create'),
    path('branches/<int:branch_id>/update/', views.branch_update, name='branch_update'),
    path('branches/<int:branch_id>/delete/', views.branch_delete, name='branch_delete'),

    path('service_categories/', views.service_category_list, name='service_category_list'),
    path('service_categories/<int:cat_id>/', views.service_category_detail, name='service_category_detail'),
    path('service_categories/create/', views.service_category_create, name='service_category_create'),
    path('service_categories/<int:cat_id>/update/', views.service_category_update, name='service_category_update'),
    path('service_categories/<int:cat_id>/delete/', views.service_category_delete, name='service_category_delete'),

    path('services/', views.service_list, name='service_list'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('services/create/', views.service_create, name='service_create'),
    # path('services/create/<int:branch_id>/', views.service_create, name='service_create'),
    path('services/<int:service_id>/update/', views.service_update, name='service_update'),
    path('services/<int:service_id>/delete/', views.service_delete, name='service_delete'),

    path('service_packages/', views.service_package_list, name='service_package_list'),
    path('service_packages/<int:package_id>/', views.service_package_detail, name='service_package_detail'),
    path('service_packages/create/', views.service_package_create, name='service_package_create'),
    path('service_packages/<int:package_id>/update/', views.service_package_update, name='service_package_update'),
    path('service_packages/<int:package_id>/delete/', views.service_package_delete, name='service_package_delete'),

    # path('users/', views.user_list, name='user_list'),
    # path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    # path('users/create/', views.user_create, name='user_create'),
    # path('users/<int:user_id>/update/', views.user_update, name='user_update'),
    # path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),

    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('bookings/create/', views.booking_create, name='booking_create'),
    path('bookings/<int:booking_id>/update/', views.booking_update, name='booking_update'),
    path('bookings/<int:booking_id>/delete/', views.booking_delete, name='booking_delete'),

    path('payments/', views.display_payments, name='payment_list'),
    path('profile/', views.profile, name="profile"),

    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:product_id>/update/', views.product_update, name='product_update'),
    path('products/<int:product_id>/delete/', views.product_delete, name='product_delete'),

   #=============================ACCOUNTS RELATED======================================#
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),


    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:employee_id>/update/', views.employee_update, name='employee_update'),
    path('employees/<int:employee_id>/delete/', views.employee_delete, name='employee_delete'),

    path('invoice/<int:booking_id>/', views.InvoicePDFView.as_view(), name='invoice_pdf'),





]
