import _thread
import time
DELAY=1 #tiempo que espera en cada seccion
NT=25  #numero de threads
choosing=[False]*NT
number=[0]*NT
critical=[False]*NT #se usa para monitorear que threads estan en la seccion critica en un momento dado
#retorna el numero maximo en el arreglo de numeros
def max_number():
    global choosing
    global number
    max=-1
    for i in number:
        if(i>max):
            max=i
    return max
#hace la comparacion de tuplas
def comparacion_tuplas(a,b,c,d):
    if(a<c):
        return True
    elif (a==c and b<d):
        return True
    return False
def lock(i):
    global choosing
    global number
    choosing[i]=True
    number[i]=max_number()+1
    choosing[i]=False
    for j in range(NT):
        while(choosing[j]):
            continue
        while(number[j]!=0 and comparacion_tuplas(number[j],j,number[i],i)):
            continue
def unlock(i):
    global choosing
    global number
    number[i]=0
def ejecutar_thread(i):
    while(True):
        #entra a la seccion critica
        lock(i)
        #print("Thread "+str(i)+" en seccion critica\n")
        critical[i]=True
        time.sleep(DELAY)
        critical[i]=False
        #sale de la seccion critica
        unlock(i)
        #print("Thread "+str(i)+" fuera de seccion critica\n")
        time.sleep(DELAY)
#monitorea en que seccion estan los threads
#True: en la seccion critica
#False: fuera de ella
def monitorear():
    tiempo=1
    while(True):
        print ("Tiempo: "+str(tiempo))
        #solo puede haber un True en el vector que se imprime
        #porque solo hay un thread en la seccion critica a la vez
        print(critical)
        tiempo+=1
        time.sleep(1)
def bakery():
    for i in range(NT):
        _thread.start_new_thread( ejecutar_thread, (i,) )
bakery()
monitorear()

    
    
