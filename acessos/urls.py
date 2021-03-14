from django.urls import path
from .views import acessos_edit, index
from .views import acessos_new, acessos_list, lista_areas, all_areas

urlpatterns = [
    path('', index, name='index'),
    path('novo/', acessos_new, name='acessos_new'),
    path('list/', acessos_list, name='acessos_list'),
    path('edit/<int:id>', acessos_edit, name='acessos_edit'),
    path('relatorio/<int:id>', lista_areas, name='lista_areas'),
    path('areas', all_areas, name='all_areas')
]
