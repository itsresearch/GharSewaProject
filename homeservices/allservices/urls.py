# allservices/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('appliance/', views.book_service, name='book_appliance'),
    path('cleaning/', views.book_service,name='book_cleaning'),
    path('electrical/', views.book_service, name='book_electrical'),
    path('flooring/', views.book_service, name='book_flooring'),
    path('painting/', views.book_service, name='book_painting'),
    path('plastering/', views.book_service, name='book_plastering'),
    path('plumbing/', views.book_service, name='book_plumbing'),
    path('roofing/', views.book_service, name='book_roofing'),
    
    path('booking_success/', views.booking_success, name='booking_success'), 
    

]


