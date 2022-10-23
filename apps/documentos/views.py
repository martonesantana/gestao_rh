from .models import Documento
from django.views.generic import CreateView
from django.urls import reverse


# Create your views here.
class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def get_success_url(self):
        return reverse('edit_funcionarios', args=[self.kwargs['funcionario_id']])