from random import randint, uniform, choice
def tranformaListaDicionarioNumerico(lista):
  
        dicionario  = {}
        for i in range(len(lista)):
            dicionario[i] = lista[i] 
        return dicionario



######################GGAME
def truncar(numero, casas_decimais):
    fator = 10 ** casas_decimais
    return int(numero * fator) / fator
def num_aleat(dig,cmc = 0,unid=0 ): #quantidade de digitos do numero, comeco do laço, valor minimo casa unidades, 
    valor1 = []
    print(f'{cmc} + {dig}')
    for i in range(cmc,dig):
        if i == 0:
            
            aux1 = randint(unid,9)


        elif i <=  dig - 1:
            aux1 = randint(1,9)
           
        valor1.append(aux1)


    valor1.reverse()
    print(valor1)
    val = int(''.join(map(str,valor1)))

    return int(val)
def multiplo_de(mul, valormax):
    aux = valormax // mul
    return mul * randint(1,aux)
def de_zero():
    while True:
         x = randint(0,9)
         y = randint(0,9)

         if x + y == 10:
             break
    return x, y
def soma(op = 'aleatorio'):
    '''
    0 - Soma das unidades da 0 
    1 - Dezena + Dezena
    2 - Dezena + Dezena igual com terminação diferente de 0
    3 - Centena + dezena
    4 - Centena + centena, com terminação diferente de  0
    5 - centenas multiplas de 100
    6 - Numeros com terminações 5
    7 - Aleatório
    '''
        
    comeco = 0
    fim = 6
    if op == 'aleatorio' or op == fim +1:
        op = randint(comeco,fim)
    sinal = '+'

    if op == 0:
         aux1, aux2 = de_zero()
         dig  =randint(2,3)
         num = ''.join([str(num_aleat(dig,1)), str(aux1)])
         num2 =''.join([str(num_aleat(dig,1)), str(aux2)])
    elif op ==1:
         num  = num_aleat(2)
         num2 = num_aleat(2)
    elif op ==2:
        num = randint(1,9)  + randint(1,9)
        num2 =  num
    elif op == 3:
        num = num_aleat(3)
        num2 = num_aleat(2)
    elif op  == 4: 
        num = num_aleat(3,1)
        num2 = num_aleat(3,1)
    elif  op ==5:
        num = str(randint(1,9)) + str(randint(1,9) * 100) #retorna um numero do tipo xy00
        num2 = str(randint(1,9)) + str(randint(1,9) * 100)
    elif op == 6:
        dig = randint(2,3)
        dig2 = randint(2,3)
        print(f'{dig} = {dig2}')
        
        num = str(num_aleat((dig-1),0,1)) + '5' # começo = 0, já ta como defaulta, porém unid igual a um não, porque se fosse um numero de dois digitos por ex iria um pro num_aleat e ai se saisse 0 iria ficar só mais 5
      
       
        num2 = str(num_aleat((randint(2,3) - 1),0,1)) + '5'   
       # esse  if dig == 2  else 1 quer dfizer que se for dois digitos  oalgarismo das dezenas não pode ser 0
    return num, sinal, num2,int( num) + int(num2)
def subtracao(op = 'alatorio'):

    comeco = 0
    fim = 3
    if op == 'aleatorio' or op == fim +1:
        op = randint(comeco,fim)
    sinal = '-'
    dig1 = randint(2,3)
    dig2 = randint(2,3)
    print(op)
    if op == 0:
         while True:
            if dig2 < dig1:
                aux = dig1
                dig1 = dig2
                dig2 = aux
            num = num_aleat(dig1)
            num2 = num_aleat(dig2)

            if num2 >num :
                break
    elif op ==1:
        dig = 2
        num =  num_aleat(dig)
        num2 = num_aleat(dig)
    elif op == 2:
        digMaior = randint(1,9)
        digMenor = randint(0,digMaior-1)
        num  = randint(1,9) + digMaior + randint(0,9)
        num2=randint(1,9) + digMenor + randint(0,9)

    elif op == 3:
        digMaior = randint(1,9)
        digMenor = randint(0,digMaior-1)
        num  = randint(1,9) + digMenor + randint(0,9)
        num2=randint(1,9) + digMaior + randint(0,9)

    return num, sinal, num2, num - num2

def raiz(op = 'aleatorio' ):
    comeco = 0
    fim = 1
    sinal =   '\u221A'  #símbolo de raíz

    '''
    0 - raizes de 2 a 10
    1 -raizes notaveis
    '''
    if op == 'aleatorio' or op == fim + 1:
        op  = randint(0,1)

    if op == 0:
        dicionario = {2:1.41,3:1.73,4:2,5:2.23,6:2.44,7:2.65,8:2.83,9:3,10:3.16} 
        num = randint(2,10)
        res = dicionario[num]
    elif op == 1:
        dicionario = {144:12,169:13,196:14,225:15, 256:16, 289:17, 324:18,361:19, 400:20, 441:21,484:22, 529:23,576:24, 625:25, 676:26, 729:27, 784:28,841:29
                        
                    }
        num= choice(list(dicionario.keys()))
        res = dicionario[num]
    return num, sinal, res

def quadrado():
    base = randint(11,30)
    sinal = '²'
    res = base  * base
    return base, sinal, res

def multiplicacao(op ='aleatorio') :
    comeco = 0
    fim = 5
    sinal = 'x'
    if op == 'aleatorio' or op == fim +1:
        op  = randint(comeco,fim)

    num = num_aleat((2))
    print(f'Valor op {op}')
  
    if op == 0:
        num2 = 3
    
    elif op == 1:
        num2 = 4
    elif op == 2:
        num2 = 5

    elif op == 3: 
        num = str(num_aleat(1,0,1))  + '5'  #1,0,1  para que o valor  da unidade (que no caso vai ser o valor da dezena), não retornae 0
        num2  = randint(3,10)
        
    elif op == 4:
        num2 = str(randint(2,9)) + '0'
    elif op ==5:
        num2 = randint(2,9)

    num = int(num)
    num2 = int(num2)

    return num, sinal, num2,num * num2

def divisao(op = 'aleatorio'):

    comeco = 0
    fim = 3
    sinal = '/'
    '''
    0 - Divisão por 2
    1 - Divisão 4 
    2 - Divisão por 10 com número decimal
    3 - Divisão por 5

    '''
  
    if op == 'aleatorio' or op == fim +1:
        op = randint(comeco, fim)
    
    num = num_aleat(randint(2,3))
    if op == 0:
        num2 = 2
    elif op==1:
        num2 = 4
    elif op == 2:
        num2 =5
    
    auxRes = str(num/num2).split('.')[1]
    valorATruncar = 2
    if str(auxRes == 3):
        valorATruncar = 3

    r = truncar(num/num2, valorATruncar)
    r =  int(r) if r.is_integer() else r 
    return num, sinal, num2, r

def tabuada():
    sinal  = 'x'
    p1 = randint(6,20)

    if p1 > 10:
      p2 = randint(3,5)
    else:
      p2 = randint(3,9)
    
    return p1,sinal, p2, p1*p2
def porcentagem(op = 'aleatorio'):
    lista = [5,10,20,25,40,50,60,75,80]
    comeco = 0
    fim = 2
    sinal = f'% de'
    if op == 'aleatorio' or op == fim+1:
        op = randint(comeco, fim)
    cent = choice(lista)
    if op == 0:
        num = multiplo_de(cent, 999)
    elif op == 1:
        num = num_aleat(2)
        while num %2 != 0:
            num = num_aleat(2)
    elif op ==2 : 
        num = num_aleat(2)
    return cent, sinal, num, num * cent / 100
  
def comecarGame(tipo,op1 ,op2):
      
      retorno = None
      valComSubMenu = [1,2,3,4,5,6]
      valMenuPrincipal = [1,2,3,4,5,6,7,8]
      valAleatorio = 9
      
    
      if tipo == 'geral':
          # se for geral a op1 ira passa a lista
          
          op1 = int(choice(op1)) 
          op2 = 'aleatorio' if op1 in valComSubMenu else None 
          
      elif tipo == 'especifico':
        
        op1 = int(op1)
        if op1 == valAleatorio:
            op1 = randint(1,valAleatorio-1)
            op2 = 'aleatorio'
            print(op1)
          
      
      
      if op1 in valComSubMenu:
                    
                try: 
                    op2 = int(op2)-1 # para enviar
                except:
                    pass
                print(f'op1 {op1}')
                if op1 == 1:
            
                    retorno = soma(op2)
                    
                elif op1 == 2:
                    retorno =subtracao(op2)
                elif op1 == 3:
                    retorno = multiplicacao(op2)
                elif op1 == 4:
                    retorno = divisao(op2)
                elif op1 == 5:
                    retorno = porcentagem(op2) 
                elif op1 == 6:
                    retorno = raiz(op2) 

      elif op1 ==7:
            retorno = tabuada()
      elif op1 == 8:
                
            retorno = quadrado()

      
      t1 = None
      t2 = None
      sinal = None
      res = None
      print(f'Valor retonno {retorno}')
      return retorno