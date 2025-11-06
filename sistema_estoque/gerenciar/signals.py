from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Produto, Categoria

@receiver(post_save, sender=Produto)
def atualizar_quantidade_produtos_apos_criar(sender, instance, created, **kwargs):
    if created:
        categoria = instance.categoria
        categoria.produtos_por_categoria = categoria.produtos.count()
        categoria.save()

@receiver(post_delete, sender=Produto)
def atualizar_quantidade_produtos_apos_excluir(sender, instance, **kwargs):
    categoria = instance.categoria
    categoria.produtos_por_categoria = categoria.produtos.count()
    categoria.save()
