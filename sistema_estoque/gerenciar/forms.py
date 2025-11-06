from .models import Produto
from django import forms

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome',
            'marca',
            'categoria',
            'imagem',
            'descricao',
            'preco',
            'quantidade_estoque',
            'peso_unitario',
            'peso_total',
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'block w-full rounded p-2 border',
                'placeholder': 'Nome do produto',
                'maxlength': 30
            }),
            'marca': forms.TextInput(attrs={'class': 'block w-full p-2 border', 'placeholder': 'Marca'}),
            'categoria': forms.Select(attrs={'class': 'block w-full p-2 border'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'block w-full'}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'class': 'block w-full p-2 border'}),
            'preco': forms.NumberInput(attrs={'step': '0.01', 'class': 'block w-full p-2 border'}),
            'quantidade_estoque': forms.NumberInput(attrs={'class': 'block w-full p-2 border', 'min': 0}),
            'peso_unitario': forms.NumberInput(attrs={'step': '0.01', 'class': 'block w-full p-2 border'}),
            'peso_total': forms.NumberInput(attrs={'step': '0.01', 'class': 'block w-full p-2 border'}),
        }
        labels = {
            'nome': ('Nome'),
            'marca': ('Marca'),
            'imagem': ('Imagem (PNG/JPG)'),
            'descricao': ('Descrição'),
            'preco': ('Preço (R$)'),
            'quantidadeestoque': ('Quantidade em estoque'),
            'peso_unitario': ('Peso unitário (kg)'),
            'peso_total': ('Peso total (kg)'),
        }
        help_texts = {
            'peso_total': ('Se vazio, será calculado como peso_unitario * quantidade_estoque ao salvar.'),
            'imagem': ('Tamanho máximo: 5MB. Formatos permitidos: JPG, PNG.'),
        }
        error_messages = {
            'nome': {
                'max_length': ("Nome muito longo (máx. 30 caracteres)."),
                'required': ("O nome é obrigatório."),
            },
        }
        
    def clean_imagem(self):
        imagem = self.cleaned_data.get('imagem')
        if imagem:
            tamanho = 100 * 1024 * 1024
            if imagem.tamanho > tamanho:
                raise forms.ValidationError(('A imagem é muito grande (máx. 100MB).'))
            formatos_validos = ['image/jpeg', 'image/png','iamge/svg','image/gif','image/webp']
            if hasattr(imagem, 'content_type') and imagem.content_type not in formatos_validos:
                raise forms.ValidationError(('Formato de imagem inválido. Use JPG ou PNG.'))
        return imagem
    