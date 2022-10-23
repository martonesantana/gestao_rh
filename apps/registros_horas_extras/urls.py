from django.urls import path

from .views import Horas_ExtrasList, Horas_ExtrasEdit, Horas_ExtrasDelete, Horas_ExtrasCreate

urlpatterns = [
    path('', Horas_ExtrasList.as_view(), name='list_horas_extras'),
    path('create/', Horas_ExtrasCreate.as_view(), name='create_horas_extras'),
    path('edit/<int:pk>', Horas_ExtrasEdit.as_view(), name='edit_horas_extras'),
    path('delete/<int:pk>', Horas_ExtrasDelete.as_view(), name='delete_horas_extras'),
]
