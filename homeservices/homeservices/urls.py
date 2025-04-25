from django.contrib import admin
from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'), 
    path('', include('users.urls')),
]