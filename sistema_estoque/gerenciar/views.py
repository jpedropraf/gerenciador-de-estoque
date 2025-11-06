from django.shortcuts import render
from .models import Produto 
from django.views.generic import CreateView ,ListView , UpdateView, DeleteView , TemplateView
from django.urls import reverse_lazy
from .forms import ProdutoForm
from django.shortcuts import redirect
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'gerenciar:dashboard.html'
    def get(self, request):
        return render(request, 'gerenciar/dashboard.html')


class CriarProduto(CreateView):
    model = Produto
    success_url = 'gerenciar:listar_produto'
    login_url = reverse_lazy('usuarios:login')
    fields = '__all__'
    template_name = 'gerenciar:adicionar_produto.html'

    def get(self,request, *args,**kwargs):
        form = ProdutoForm()
        return render(request, 'gerenciar/produto_form.html', {'form': form})
    def post(self,request, *args,**kwargs):
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto criado com sucesso!")
            return redirect("oficina_app:listar_produtos")
        messages.error(request, "Erro ao criar produto.")
        return render(request, self.template_name, {"form": form})

class ListarProduto(ListView):
    model = Produto
    template_name = 'produtos/listar_produtos.html'
    context_object_name = 'produto'  
    reverse_lazy('gerenciar:listar:produto')
    login_url = reverse_lazy('usuarios:login')
    fields = '__all__'
    
    def get(self, request, *args, **kwargs):
        try:
            produtos = self.get_queryset()
            if produtos.exists():
                messages.success(request, "Produtos listados com sucesso!")
            else:
                messages.info(request, "Nenhum produto encontrado.")
            return render(request, self.template_name, {"produtos": produtos})

        except Exception as e:
            messages.error(request, "Erro ao listar produtos.")
            return render(request, self.template_name, {"produtos": []})
       
    
    
class EditarProduto(UpdateView):
    model = Produto
    template_name = 'produtos/editar_produtos.html'
    context_object_name = 'produto'  
    reverse_lazy('gerenciar:listar:produto')
    login_url = 'usuarios:login'
    fields = [
    'nome','marca','categoria','imagem','descricao','preco','quantidade_estoque','data_adicionado','data_atualizado','peso_unitario','peso_total',
]

    def get(self, request, *args, **kwargs):
        form = ProdutoForm(instance=self.get_object())
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = ProdutoForm(request.POST, request.FILES, instance=self.get_object())
        if form.is_valid():
            form.save()
            messages.success(request, "Produto editado com sucesso!")
            return redirect("oficina_app:listar_produtos")
        messages.error(request, "Erro ao editar produto.")
        return render(request, self.template_name, {"form": form})
    
class DeletarProduto(DeleteView):
    model = Produto
    template_name = 'produtos/editar_produtos.html'
    context_object_name = 'produto'  
    success_url = reverse_lazy('gerenciar:listar:produto')
    login_url = 'usuarios:login'

    def get(self, request ,*args, **kwargs):
        produto = self.get_object()
        return render(request, self.template_name, {"produto": produto})

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        messages.success(request, "Produto excluído com sucesso!")
        return redirect("oficina_app:listar_produtos")