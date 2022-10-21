from django.db import models
from apps.empresas.models import Empresa
from django.urls import reverse

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do departamento')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('list_departamentos')