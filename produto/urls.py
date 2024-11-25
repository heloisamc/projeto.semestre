from django.urls import path
from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView, ProdutoCreateView, ProdutoDeleteView, ProdutoListView, ProdutoUpdateView

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nova/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/excluir/', CategoriaDeleteView.as_view(), name='categoria_delete'),
   
    path('produto/', ProdutoListView.as_view(), name='produto_list'),
    path('produto/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produto/<int:pk>/editar/',ProdutoUpdateView.as_view(), name='produto_update'),
    path('produto/<int:pk>/excluir/',ProdutoDeleteView.as_view(), name='produto_delete'),
]