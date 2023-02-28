'''
Nombre: Carolain Jimenez Bedoya
Asignatura: Sistemas Operativos
Memoria es un diccionario donde se almacenaran los valores de las instrucciones, y las instrucciones de un proceso.'''

memoria = dict()
memoria={}
ICR= 1 
acumulador=0
array= [] 

''' funcionSET, recibe una lista y un diccionario, la lista conforma una instrucción en la cual se determina el espacio donde se requiere determinado valor, si este no existe, el espacio de memoria se crea en el diccionario=memoria'''

def funcionSET(valor,diccionario):
     keys= diccionario.keys()
      
     if valor[1] in keys :
        diccionario[valor[1]] = valor[2]
     else:
        diccionario[valor[1]] = valor[2]
        return diccionario

'''funcionLDR, recibe una lista (instruccion) y un diccionario(memoria), y con la variable global del acumulador, envia el valor del espacio de memoria que se requiere al acumulador'''
 
def funcionLDR(valor,diccionario):
  global acumulador
  acumulador= int(diccionario.get(valor[1]))
  return acumulador

''' funcionADD, recibe una lista(Instrucción) y un diccionario(memoria), posee tres formas de realizarse, sin embargo, su funcionamiento es el mismo, determinar el valor existente en una determinada posición, y le aumenta (suma) dicho valor al acumulador. Pueden ser 2 valores o en el último caso, guardar dicho valor en la última posición especificada, ya existente. '''
  
def funcionADD(valor,memoria): 
   global acumulador
   if valor[2] == "NULL":

     valor = int(memoria.get(valor[1]))
     acumulador += valor
   elif valor[3] == "NULL":

     valor1 = int(memoria.get(valor[1]))
     valor = int(memoria.get(valor[2]))
     suma= valor1+valor
     acumulador += int(suma)
     
   elif valor[4] == "NULL":
  
     valor3= int(memoria.get(valor[1])) + int(memoria.get(valor[2]))
     memoria[valor[3]]= valor3
     valor1 = int(memoria.get(valor[1]))
     valor = int(memoria.get(valor[2]))
     suma= valor1+valor
     acumulador += int(suma)


''' funcionMUL, funciona de la misma manera que la fucionADD, la unica diferencia es el operador, ya que este operador es de multiplicación. '''
     
def funcionMUL(valor,memoria): 
   global acumulador
   if valor[2] == "NULL":

     valor = int(memoria.get(valor[1]))
     acumulador *= valor
     
   elif valor[3] == "NULL":
     valor1 = int(memoria.get(valor[1]))
     valor = int(memoria.get(valor[2]))
     multiplicacion= valor1*valor
     acumulador += int(multiplicacion)
     
   elif valor[4] == "NULL":
     
     valor3= int(memoria.get(valor[1])) * int(memoria.get(valor[2]))
     memoria[valor[3]]= valor3
     valor1 = int(memoria.get(valor[1]))
     valor = int(memoria.get(valor[2]))
     multi= valor1*valor
     acumulador += int(multi)


'''Funcion SUB, funciona de la misma manera que la fucionADD, la unica diferencia es el operador, ya que este operador es de resta.'''
     
def funcionSUB(valor,memoria): 
   global acumulador
   if valor[2] == "NULL":

     valor = int(memoria.get(valor[1]))
     acumulador -= valor
   elif valor[3] == "NULL":

     valor1 = int(memoria.get(valor[1]))
     valor = int(memoria.get(valor[2]))
     resta= valor1-valor
     acumulador += int(resta)
  
     
   elif valor[4] == "NULL":
     valor3= int(memoria.get(valor[1])) - int(memoria.get(valor[2]))
     memoria[valor[3]]= valor3
     valor1 = int(memoria.get(valor[1]))
     valor = int(memoria.get(valor[2]))
     resta= valor1-valor
     acumulador -= int(resta)

'''Funcion DIV, funciona de la misma manera que la fucionADD, la unica diferencia es el operador, ya que este operador es de división. '''
     
def funcionDIV(valor,memoria): 
   global acumulador
   if valor[2] == "NULL":
     valor = int(memoria.get(valor[1]))
     acumulador /= valor
     
   elif valor[3] == "NULL":
     valor1 = int(memoria.get(valor[1]))
     valor = int(memoria.get(valor[2]))
     division= valor1/valor
     acumulador /= int(division)
     
   elif valor[4] == "NULL":
     valor3= int(memoria.get(valor[1])) / int(memoria.get(valor[2]))
     memoria[valor[3]]= valor3
     valor1 = int(memoria.get(valor[1]))
     valor = int(memoria.get(valor[2]))
     division= valor1/valor
     acumulador /= int(division)

'''La funcion STR recibe una lista(Instruccion) y un diccionario(memoria),toma la variable global acumulador y saca su valor, seguidamente determina la posicion de la memoria a la que se le debe asignar el valor, y actualiza la memoria, si el espacio de memoria no existe, esta función lo crea. ''' 
def funcionSTR(valor,memoria):
  global acumulador

  keys= memoria.keys() 
  
  if valor[1]  not in keys :
    memoria[valor[1]] = acumulador
  else:
  
    for key, value in memoria.items():
      if key == valor[1]:
        memoria[key] = acumulador

'''funcionINC, recibe una lista(instruccion) y un diccionario(memoria) cargar el valor en la dirección de memoria D3 suma 1 y almacena en la misma dirección'''

def funcionINC(valor,memoria): 
  valor1= int(memoria.get(valor[1]))+1
  memoria[valor[1]]= valor1

'''funcionDEC, recibe una lista(instruccion) y un diccionario(memoria) cargar el valor en la dirección de memoria D3 resta 1 y almacena en la misma dirección'''

def funcionDEC(valor,memoria): 
  valor1= int(memoria.get(valor[1]))-1
  memoria[valor[1]]= valor1


'''funcionSHW, recibe una lista(instruccion) y un diccionario(memoria), toma una posicion de memoria de la instruccion y muestra en pantalla su valor.Tambien, muestra el valor del acumulador si se le indica, aún no se ha determinado como imprimir el MAR, MDR e ICR.'''

def funcionSHW(valor,memoria):
    if(valor[1]== "ACC"):
      global acumulador
      print(acumulador)
    else:
      mostrar = int(memoria[valor[1]])
      print(mostrar)

''' borrarMemoria, elimina los valores de la memoria, una vez que el proceso ha terminado su ejecución'''

def borrarMemoria(diccionario):
  diccionario.clear()

'''hallarFuncion, recibe una lista(instruccion) y determina cual es la palabra de inicio para identificar la funcion a realizar.'''

def hallarFuncion(lista):
  if lista[0]== "SET":
      funcionSET(lista,memoria)
      

  if lista[0]== "LDR":
       funcionLDR(lista,memoria)

  if lista[0]== "STR":
       funcionSTR(lista,memoria)

  if lista[0]== "ADD":
       funcionADD(lista,memoria)
      
  if lista[0]== "SHW":
       funcionSHW(lista,memoria)

  if lista[0]== "MUL":
      funcionMUL(lista,memoria)

  if lista[0]== "INC":
      funcionINC(lista,memoria)

  if lista[0]== "DEC": 
    funcionDEC(lista, memoria)

  if lista[0]== "SUB":
    funcionSUB(lista, memoria)

  if lista[0]== "DIV": 
    funcionDIV(lista,memoria)
     
  if lista[0]== "END":
    print("acabar")
    print(memoria)
    borrarMemoria(memoria)
    global ICR
    ICR=1
    global acumulador
    acumulador=0

''' cargarInstrucciones, es la función que carga las instrucciones al diccionario que actua como memoria principal''' 
  
def cargarInstrucciones(lista,memoria):
  global ICR
  i=0
  for i in range(len(lista)):
    memoria[ICR]= lista[i]
    ICR+=1
  i+=1
  return ICR


'''cicloBasicoInstrucciones, Ejecuta un solo proceso de un archivo, donde cada instruccion es puesta en un array(lista), además, carga las instrucciones a la memoria y luego itera cada elemento de la lista externa y evalua la instruccion que debe ejecutarse.'''

def cicloBasicoInstrucciones(archivo):
 with open(archivo) as fname:
  lista=[]
  for lineas in fname:
	   lista.append(lineas.split())

  cargarInstrucciones(lista,memoria)
  i=0
  for i in range(len(lista)):
    hallarFuncion(lista[i]) 
  i+=1

cicloBasicoInstrucciones("archivo1.txt") 
cicloBasicoInstrucciones("archivo.txt") 
cicloBasicoInstrucciones("archivo3.txt")

