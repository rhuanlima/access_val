from django.urls import path
from .views import index
from .views import acessos_new

urlpatterns = [
    path('', index, name='index'),
    path('novo/', acessos_new, name='acessos_new')
]
