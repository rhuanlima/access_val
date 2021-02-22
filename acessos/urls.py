from django.urls import path
from .views import acessos_edit, index
from .views import acessos_new, acessos_list

urlpatterns = [
    path('', index, name='index'),
    path('novo/', acessos_new, name='acessos_new'),
    path('list/', acessos_list, name='acessos_list'),
    path('edit/<int:id>', acessos_edit, name='acessos_edit')
]
