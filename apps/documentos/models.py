from tabnanny import verbose
from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario

# Create your models here.

class Documento(models.Model):
    descricao = models.CharField(max_length=200, help_text='Descrição do documento')
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
    
    def get_absolute_url(self):
        return reverse('edit_funcionarios',args=[self.pertence.id])
    
    
    def __str__(self):
        return self.descricao