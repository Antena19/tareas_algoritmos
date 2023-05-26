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
    listaConcursante.append(numConcursante); 
print(f"Sus números de la suerte son: {listaConcursante}"); #muestro los números del concursante.
print("---Sorteo 1---");
print("Los números ganadores son: ");
for x in range(5): #hice un for para seleccionar los 5 números ganadores
    numPosibles = random.randint(1,50); #uso el random para sacarlos al azar
    print(numPosibles); #muestro los números que salieron al azar
if listaConcursante != numPosibles: #comparo los números del concrsante con los del sorteo, si son diferentes...
    print("Lo siento, no ha ganado esta ronda") #muestro mensaje de que perdió
else: #si son iguales...
    print("¡¡¡Felicidades!!! ¡¡Ganó!!");#muestro mensaje de que ganó
