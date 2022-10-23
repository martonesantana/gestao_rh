from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models import Sum


from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento, default=None)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, default=None)
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('list_funcionarios')
    
    @property
    def total_horas_extras(self):
        total = self.registrohoraextra_set.all().aggregate(Sum('horas'))['horas__sum']
        return total