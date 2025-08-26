from django.shortcuts import render, redirect
from django.http import HttpResponse    
from functions import *
from calculoMental.views import *
from calculoMental.models import *
from django.conf import settings
# Create your views here.
def redirectInicial(request):
    return redirect('/inicio/')
def loadInicio(request):
    return render(request, 'inicio.html')
def redirectGameIntermedium(request, partidaId = 'error'):
    return redirect(f'/jogando/partida/{(partidaId)}')

def loadMenu(request, qualMenu, valorDigitado = None):
   
        
    if qualMenu == 'especifico':
        if request.method == 'POST':
            subMenus =  [1,2,3,4,5,6]
            
            valorDigitado = int(request.POST.get('input')) 
            
            if valorDigitado in subMenus:
                qualMenu = '2'
                return redirect(f'/menu/{qualMenu}/{valorDigitado}')
            else: 
                partida  = Partida(
                 tipo='especifico',
                 op1=valorDigitado    

             )
                partida.numero = Partida.objects.all().count()+ 1
                partida.save()
                

                return redirectGameIntermedium(request,partida.id)

        textMenu = settings.MENU_VALORES
        dicionarioMenu  = tranformaListaDicionarioNumerico(textMenu)
        
        
        return render(request, 'menu.html', {'dicionarioMenu': dicionarioMenu, 'qualMenu': qualMenu, 'tipoMenu':qualMenu})
    elif qualMenu == 'geral':
        if request.method == 'POST':
            dados_request = list(request.POST.values())
            dados_numericos = []
            for i in dados_request:
                if i.isdigit():
                    dados_numericos.append(int(i)+1) # i +1 pq os dados no menu taavam começando em 0 porém na hora de começar lá comecei em 1 
            partida = Partida(
                tipo='geral'
            )
            partida.numero = Partida.objects.all().count()+ 1


            partida.save()
            dado = ''
            for i in dados_numericos:
                dado = dado + str(i) + ','
            return redirectGameIntermedium(request, f'{partida.id}|{dado}') 
        textMenu = ["Soma", "Subtração","Multiplicação","Divisão","Porcentagens notáveis","Raiz","Tabuada","Aleatório"]
        dicionarioMenu  = tranformaListaDicionarioNumerico(textMenu)
        
        
        return render(request, 'menu.html', {'dicionarioMenu': dicionarioMenu, 'qualMenu': qualMenu, 'tipoMenu':qualMenu})
    elif qualMenu =='2':
        
        if request.method == 'POST':
             partida  = Partida(
                 tipo='especifico',
                 op1=int(request.POST.get('opcao1')),
                 op2=int( request.POST.get('input'))
             )
             partida.numero = Partida.objects.all().count()+ 1

             partida.save()
             return  redirectGameIntermedium(request, partida.id)
        listaSub = settings.SUB_MENU_VALORES
        
    
        subMenu = tranformaListaDicionarioNumerico(listaSub[valorDigitado-1])

        qualMenu= int(qualMenu)
        return render(request, 'menu.html',{'dicionarioMenu': subMenu, 'qualMenu':qualMenu, 'valorDigitado':valorDigitado, 'tipoMenu': 'especifico'})
    
    return HttpResponse('parte não projetad')
