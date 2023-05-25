'''Juego de Azar'''
#La empresa de juegos de azar “Lotín”, desea crea una aplicación móvil que genere sorteos rápidos dentro del mismo celular.
#Para eso, le solicita crear un algoritmo que genere una lista de números de manera aleatoria donde si usted acierta, gana. Las reglas son las siguientes:
#Los números participantes son del 1 al 49
#El jugador debe elegir 5
#Se generará 1 ronda
#Si el jugador acierta a los números mostrará un mensaje de ganador.
print("----Bienvenido a Lotín----");
numGanadores=[]; #creo lista de 5 números ganadores
for i in range(5):
    numConcursante=int(input("Ingrese un número: "));
