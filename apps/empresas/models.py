from tabnanny import verbose
from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.nome