from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    produtos_por_categoria = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    categoria = models.ForeignKey(
        Categoria,
        related_name='produtos',
        on_delete=models.CASCADE
    )
    imagem = models.ImageField(upload_to='produtos/media/', null=True, blank=True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    data_adicionado = models.DateTimeField(auto_now_add=True)
    data_atualizado = models.DateTimeField(auto_now=True)
    peso_unitario = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    peso_total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

   

    def __str__(self):
        return f"{self.nome} - {self.marca}"
