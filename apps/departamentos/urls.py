from django.urls import path


from .views import DepartamentoList, DepartamentoEdit, DepartamentoDelete, DepartamentoCreate





urlpatterns = [
    path('', DepartamentoList.as_view(), name='list_departamentos'),
    path('create/', DepartamentoCreate.as_view(), name='create_departamentos'),
    path('edit/<int:pk>', DepartamentoEdit.as_view(), name='edit_departamentos'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamentos'),
]