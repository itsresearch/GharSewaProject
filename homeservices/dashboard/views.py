from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Sum, Count
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from allservices.models import ServiceBooking
import json
from allservices.forms import ServiceBookingForm

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def user_dashboard(request):
    today = timezone.now().date()
    month_start = today.replace(day=1)

    bookings_count = ServiceBooking.objects.filter(created_at__gte=month_start).count()
    revenue = ServiceBooking.objects.filter(created_at__gte=month_start).aggregate(total=Sum('revenue'))['total'] or 0
    year_start = today.replace(month=1, day=1)
    # Count distinct customers by email instead of user
    customers_count = ServiceBooking.objects.filter(created_at__gte=year_start).values('email').distinct().count()
    pending_bookings = ServiceBooking.objects.filter(preferred_date=today, status='pending')
    completed_services_today = ServiceBooking.objects.filter(preferred_date=today, status='completed').count()

    top_services = (ServiceBooking.objects
                    .filter(created_at__gte=month_start)
                    .values('service')
                    .annotate(total_requests=Count('id'), total_revenue=Sum('revenue'))
                    .order_by('-total_requests')[:5])

    context = {
        'bookings_count': bookings_count,
        'revenue': revenue,
        'customers_count': customers_count,
        'pending_bookings': pending_bookings,
        'completed_services_today': completed_services_today,
        'top_services': top_services,
    }
    return render(request, 'dashboard/user_dashboard.html', context)

@require_POST
@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def update_booking_status(request):
    try:
        data = json.loads(request.body)
        booking_id = data.get('booking_id')
        new_status = data.get('status')

        booking = ServiceBooking.objects.get(id=booking_id, status='pending')
        if new_status == 'completed':
            booking.status = 'completed'
            booking.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid status'})
    except ServiceBooking.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Booking not found or already processed'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def profile(request):
    return render(request, 'dashboard/user_profile.html')

@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return render(request, 'registration/logout.html')

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def service_bookings(request):
    bookings = ServiceBooking.objects.all()  # Admin can see all bookings
    return render(request, 'dashboard/service_bookings.html', {'bookings': bookings})

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def view_booking(request, booking_id):
    try:
        booking = ServiceBooking.objects.get(id=booking_id)
    except ServiceBooking.DoesNotExist:
        messages.error(request, "Booking not found.")
        return redirect('service_bookings')
    return render(request, 'dashboard/view_booking.html', {'booking': booking})

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def edit_booking(request, booking_id):
    try:
        booking = ServiceBooking.objects.get(id=booking_id)
    except ServiceBooking.DoesNotExist:
        messages.error(request, "Booking not found.")
        return redirect('service_bookings')

    if request.method == 'POST':
        form = ServiceBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully!")
            return redirect('service_bookings')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ServiceBookingForm(instance=booking)
    return render(request, 'dashboard/edit_booking.html', {'form': form, 'booking': booking})

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def delete_booking(request, booking_id):
    try:
        booking = ServiceBooking.objects.get(id=booking_id)
        booking.delete()
        messages.success(request, "Booking deleted successfully!")
    except ServiceBooking.DoesNotExist:
        messages.error(request, "Booking not found.")
    return redirect('service_bookings')