# views.py
from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from datetime import date, timedelta
from .models import Booking

def payment_report(request):
    # Default to today if start_date or end_date not provided
    start_date = request.GET.get('start_date', timezone.now().date())
    end_date = request.GET.get('end_date', timezone.now().date())

    # Convert start_date and end_date from string to date objects
    # start_date = timezone.datetime.strptime(start_date, "%Y-%m-%d").date()
    # end_date = timezone.datetime.strptime(end_date, "%Y-%m-%d").date()

    # Todays Collection
    today_collection = Booking.objects.filter(created_at__date=start_date, payment_status=True).aggregate(Sum('service_amount'))['service_amount__sum'] or 0

    # Weekly Collection
    weekly_collection = Booking.objects.filter(created_at__date__range=[start_date, end_date], payment_status=True).aggregate(Sum('service_amount'))['service_amount__sum'] or 0

    # Monthwise Collection
    monthly_collection = Booking.objects.filter(created_at__date__range=[start_date, end_date], payment_status=True).aggregate(Sum('service_amount'))['service_amount__sum'] or 0

    context = {
        'start_date': start_date,
        'end_date': end_date,
        'today_collection': today_collection,
        'weekly_collection': weekly_collection,
        'monthly_collection': monthly_collection,
    }

    return render(request, 'reports/payments/payment_report.html', context)
