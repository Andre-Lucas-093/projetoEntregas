from django.db import models

class Membro(models.Model):
  nome = models.CharField(max_length=255)
  codigo = models.CharField(max_length=255)
  slug = models.SlugField(default="", null=False)

  def __str__(self):
    return self.nome

class Entrega(models.Model):
    data_entrega = models.DateField()
    vendedor = models.ForeignKey(Membro, on_delete=models.CASCADE)
    veiculo = models.CharField(max_length=10, choices=[("carro", "Carro"), ("moto", "Moto")])
    endereco = models.CharField(max_length=255)
    distancia = models.FloatField(null=True, blank=True)
    horario = models.CharField(max_length=10, choices=[("manha","Manhã"),("tarde","Tarde")])