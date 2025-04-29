# allservices/views.py
from django.shortcuts import render, redirect
from .models import ServiceBooking


def book_service(request):
    if request.method == 'POST':
        # Create a ServiceBooking object and save the data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        service = request.POST.get('service')
        preferred_date = request.POST.get('preferred_date')

        # Create a new ServiceBooking object and save it to the database
        booking = ServiceBooking(
            name=name,
            email=email,
            phone=phone,
            address=address,
            service=service,
            preferred_date=preferred_date
        )
        booking.save()

        # Redirect after saving the form data
        return redirect('booking_success')  # Redirect to a thank you page or another page after form submission

    # return render(request, 'service/cleaning.html')


def booking_success(request):
    return render(request, 'service/booking_success.html')