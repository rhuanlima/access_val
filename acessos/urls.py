from django.urls import path
from acessos import views


urlpatterns = [
    path('', views.index, name='index')
]
