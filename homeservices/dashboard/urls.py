from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    path('profile/', views.profile, name='user_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('update_booking_status/', views.update_booking_status, name='update_booking_status'),
    path('service-bookings/', views.service_bookings, name='service_bookings'),
    path('service-bookings/view/<int:booking_id>/', views.view_booking, name='view_booking'),
    path('service-bookings/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('service-bookings/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]