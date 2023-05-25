'''Juego de Azar'''
#La empresa de juegos de azar “Lotín”, desea crea una aplicación móvil que genere sorteos rápidos dentro del mismo celular.
#Para eso, le solicita crear un algoritmo que genere una lista de números de manera aleatoria donde si usted acierta, gana. Las reglas son las siguientes:
#Los números participantes son del 1 al 49
#El jugador debe elegir 5
#Se generará 1 ronda
#Si el jugador acierta a los números mostrará un mensaje de ganador.
print("----Bienvenido a Lotín----");
numPosibles = list(range(1,50)); #Creo la lista de los posibles números ganadores. Uso range para decir que quiero los números del 1 al 49. Uso list para transformar el range a lista.
print(f" Números posibles: {numPosibles}"); #muestro los números posibles.
listaConcursante=[]; #creo una lista vacía del concursante
for i in range(5): #repito 5 veces...
    numConcursante=int(input("Ingrese un número: "));
