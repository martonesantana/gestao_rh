from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do departamento')
    
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    
    def __str__(self):
        return self.nome