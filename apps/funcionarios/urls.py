from django.urls import path

from apps.funcionarios.views import FuncionarioList, FuncionarioEdit, FuncionarioDelete, FuncionarioCreate

urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionarios'),
    path('create/', FuncionarioCreate.as_view(), name='create_funcionarios'),
    path('edit/<int:pk>', FuncionarioEdit.as_view(), name='edit_funcionarios'),
    path('delete/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionarios'),
]
