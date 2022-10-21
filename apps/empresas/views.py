from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse

from apps.empresas.models import Empresa

# Create your views here.

class EmpresaCreate(CreateView):
    model = Empresa
    fields=['nome',]
    
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Empresa criada com sucesso')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields=['nome',]
    
    def get_object(self):
        funcionario = self.request.user.funcionario
        return funcionario.empresa

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Empresa editada com sucesso')
    