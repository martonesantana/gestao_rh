from tabnanny import verbose
from django.db import models

from apps.funcionarios.models import Funcionario

# Create your models here.

class Documento(models.Model):
    descricao = models.CharField(max_length=200, help_text='Descrição do documento')
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
    
    def __str__(self):
        return self.descricao