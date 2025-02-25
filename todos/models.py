from django.db import models

class Todo(models.Model):
    title = models.CharField(verbose_name='Titulo',max_length=100, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False) #sera implementado automaticamente referente a criação
    deadline = models.DateField(verbose_name='Data de entega',null=False, blank=False)
    finished_at = models.DateField(null=True)
    
    class Meta():
        ordering = ["deadline"]