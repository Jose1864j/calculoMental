from django.shortcuts import render,redirect
from django.http import HttpResponse
from functions import *
from .models import * 
from django.conf import settings
# Create your views here.

def jogar(request, idPartida):
    try:
        partida = Partida.objects.get(id=int(idPartida))
        tipo = partida.tipo
        op1 = partida.op1
        op2 = partida.op2
    except:
        didivido  =  idPartida.split('|')
        partida = Partida.objects.get(id=int(didivido[0]))
        op1 = []
        listaOpcoes = didivido[1].split(',')
        tipo = partida.tipo
        for i in listaOpcoes:
            op1.append(i)
        
    if request.method == 'POST': #ja ta jogando
       respostaCerta = request.POST.get('resposta')
       respostaUsuario = request.POST.get('respostaUsuario')
       respostaUsuario = " ".join(respostaUsuario.split())
       print(f'Respsota usuario: {respostaUsuario}- respostaCerta {respostaCerta}.')
       if respostaCerta == respostaUsuario:
          partida.acertos+=1
          partida.totais+=1

       else:
           partida.totais+=1
       partida.save()
    if idPartida == 'error':
        return HttpResponse('Partida não criada')
    elif tipo == 'especifico':
       
        valores = comecarGame('especifico', op1,op2)
        
        if len(valores) == 3:
            v1, sinal, res = valores
            v2 = ''
        else:
            v1, sinal, v2,res = valores

        return render(request, 'jogar.html', {'partidaId':partida.id,'tipo':tipo,'v1':v1, 'sinal':sinal, 'v2': v2, 'resposta': res})
    elif tipo == 'geral':
        op1.pop() # remove o ultimo pq ta ficando um espaco vazio no final pq tem uma virgula no final ia ao dar split(',') fica u mvazio
        valores = comecarGame('geral', op1, None)
        if len(valores) == 3:
            v1, sinal, res = valores
            v2 = ''
        else:
            v1, sinal, v2,res = valores
        return render(request, 'jogar.html', {'partidaId':partida.id,'tipo':tipo,'v1':v1, 'sinal':sinal, 'v2': v2, 'resposta': res})

    return ('Parte não feitaa')
    
def irPara(request, txt):

    if txt == 'menuEspecifico':
        return redirect('/menu/especifico')
    
    elif txt == 'menuGeral':
        return redirect('/menu/geral')
    elif txt == 'inicio':
        return redirect('/inicio/')
    elif txt == 'historico':
        return redirect('/mostrar/historico/')
    
def verificaResposta(request):
    if request.method == 'POST':
        respostaUsuario = request.POST.get('respostaUsuario')
        resposta =  request.POST.get('resposta')
        
        return HttpResponse(f'{resposta ==respostaUsuario}')
    

def finalizar(request, id):
    partida = Partida.objects.get(id=id)


    return render(request,'resultado.html', {'acertos':partida.acertos, 'erros':(partida.totais - partida.acertos), 'total': partida.totais})


def historico(request, indiceFiltrar = None, comoOrdenar  = None):
    partidas = Partida.objects.all()
    menu =settings.MENU_VALORES
    listaSub =settings.SUB_MENU_VALORES
  
    if indiceFiltrar != None and indiceFiltrar != 'None':
        indiceFiltrar = int(indiceFiltrar)
        partidas = Partida.objects.filter(op1=indiceFiltrar +1) # + 1 pq estamos começando no 1 a contagem aoa adicionar op1 e op2
    if comoOrdenar !=None and comoOrdenar != 'None':
        if comoOrdenar == 'crescente':
            partidas = partidas.order_by('id')
        else:
             partidas = partidas.order_by('-id')

    for p in partidas:
        op1Value  = p.op1
        op2Value =  p.op2
        #isto só para conseugir usar o valor de op1 ali na op2 ai peguei o op2 tabmém para fica rpadronizado 
        p.op1 = 'geral'
        p.op2 = 'geral'
        if op1Value != None:

             p.op1 = menu[op1Value-1]
        if op2Value != None:
            print(f'op1Value {op1Value} e op2 {op2Value}')
            p.op2 = listaSub[op1Value-1][op2Value-1]
        else:
            p.op2 = ' '#isto para não aparecer none no html
        setattr(p, 'erros', p.totais - p.acertos) #adiciona um campo tempeorário em partidas de erross
    return render(request, 'historico.html', {'partidas':partidas, 'itensMenu':menu})


def filtrar(request, oQue):
   # peg aonde que ta o cmainho separado por espaço
    if request.method == 'POST':
         if oQue == 'historico':
              menu =settings.MENU_VALORES
              filtrarPeloMenu = request.POST.get('filtrarPeloQ')
              indice = menu.index(filtrarPeloMenu)
              
              return redirect('historicoFiltradoOdenador', indice,None) #redireciona par aurl com esse nome


    return HttpResponse('método não é post')

def ordenar(request, oQue):

    if request.method =='POST':
        if oQue =='historico':
            crescenteEDecrescente  = request.POST.get('tipodeOrdenamento').lower()
            return redirect('historicoFiltradoOdenador', None,  crescenteEDecrescente)

    return HttpResponse('método não é post')