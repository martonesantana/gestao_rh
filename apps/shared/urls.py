from django.urls import path

from apps.shared.views import home

urlpatterns = [
    path('', home),    
]