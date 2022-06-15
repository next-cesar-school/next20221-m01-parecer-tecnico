from django.db import models
from django.utils import timezone

# Create your models here.



class ParecerDoTecnico(models.Model):
    
    equipamento = models.ForeignKey("Equipamento", on_delete=models.CASCADE, related_name='parecerdotecnico') 
    defeitoRelatado = models.CharField(max_length=50, null=False)
    diagonosticoEfetuado = models.CharField(max_length=20, null=False)
    tempoDeReparo = models.CharField(max_length=30, null=False)
    DataDoArquivo = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return self.equipamento.nome



class Equipamento(models.Model):
    STATUS_CHOICES = (
            ("1","Celular"),
            ("2","Tablet"),
            ("3","Computador"),
            ("4","TV"),
            ("5","Asistente Digital"),
            ("6","Celular"),
)
    
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='equipamento')
    tipoDeEquipamento = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    numeroDeSerie = models.CharField(max_length=20, null=False)
    fabricante = models.CharField(max_length=15, null=False)
    modelo = models.CharField(max_length=15, null=False)
    data_equipamento = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.cliente.nome



class Cliente(models.Model):

    nomeCompleto = models.CharField(max_length=50, null=False)
    documentoDeIdentificacao = models.CharField(max_length=20, null=False)
    telefone = models.IntegerField(null=False)
    email = models.CharField(max_length=30, null=False)
    cep = models.IntegerField(null=False)
    rua = models.CharField(max_length=30, null=False)
    localidade = models.CharField(max_length=30, null=False)
    cidade = models.CharField(max_length=30, null=False)
    
    


