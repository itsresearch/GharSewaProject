# allservices/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cleaning/', views.book_service, name='book_service'),
    path('booking_success/', views.booking_success, name='booking_success'),  # Add this line

    # Add other URL patterns as needed
]
