from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from django.urls import reverse_lazy

from apps.registros_horas_extras.forms import RegistroHoraExtraForm

from .models import RegistroHoraExtra

# Create your views here.

class Horas_ExtrasList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa)
        return queryset

class Horas_ExtrasEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
   
        
    def get_form_kwargs(self):
        kwargs = super(Horas_ExtrasEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    
    
class Horas_ExtrasDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_horas_extras')
    

class Horas_ExtrasCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    
    def get_form_kwargs(self):
        kwargs = super(Horas_ExtrasCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    
    
