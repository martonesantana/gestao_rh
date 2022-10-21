from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.

class FuncionarioList(ListView):
    model = Funcionario
    
    
    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa)
        return queryset

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']
    
    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa)
        return queryset

class FuncionarioDelete(DeleteView):
    model = Funcionario    
    success_url = reverse_lazy('list_funcionarios')
    
class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome','departamentos']
    
    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)
    
    
    
    