from django.urls import path
from .views import EmpresaCreate, EmpresaEdit

urlpatterns = [
    path('new', EmpresaCreate.as_view(), name='new_empresa'),
    path('edit/<int:pk>', EmpresaEdit.as_view(), name='edit_empresa'),
]