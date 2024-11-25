from django.urls import path
from .views import ProdutoSaldoView

urlpatterns = [
    path('', ProdutoSaldoView.as_view(), name='welcome'),
]