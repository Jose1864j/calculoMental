
from django.contrib import admin
from django.urls import path, include
from .views import redirectInicial, loadMenu, loadInicio, redirectGameIntermedium
from calculoMental.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',redirectInicial, name='inicio' ),
    path('inicio/', loadInicio, name='loadInicio'),
    path('menu/<str:qualMenu>/', loadMenu, name='loadMenu'),
    path('menu/<str:qualMenu>/<int:valorDigitado>', loadMenu, name='loadMenu'),
    path('calculo-mental/', include('calculoMental.urls')),
    path('redirectGameIntermedium/<str:tipo>/<int:op1>/', redirectGameIntermedium, name='redirectGameIntermedium'),
    path('redirectGameIntermedium/<str:tipo>/<int:op1>/<int:op2>/<int:idPartida>', redirectGameIntermedium, name='redirectGameIntermedium2'),
    path('jogando/',include('calculoMental.urls')),
    path('mostrar/', include('calculoMental.urls')),


]
