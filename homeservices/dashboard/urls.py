from django.urls import path
from . import views


app_name = 'dashboard'  # ✅ Required for namespacing

urlpatterns = [
    path('', views.home, name='base'),
 # name='base' should match what you're calling in the template
]
