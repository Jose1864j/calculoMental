
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('irPara/<str:txt>', irPara, name='irPara'),
   path('partida/<str:idPartida>', jogar, name='jogando'),
   path('resultado/<str:id>', finalizar, name="finalizar"),
   path('historico/',historico,  name='historico'),
   path('historico/<str:indiceFiltrar>/<str:comoOrdenar>',historico,  name='historicoFiltradoOdenador'),
   path('filtrar/<str:oQue>/', filtrar, name='filter'),
   path('ordenar/<str:oQue>/', ordenar, name='ordenar')


   
   ]
