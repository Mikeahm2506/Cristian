""""
   Algoritmo de Cristian
   Codigo Servidor
   Hernandez Martinez miguel Angel 
   Nava Manuel
"""
#librerias
from socket import*
from datetime  import* 

#Servidor
addSever = "localhost"
portSever = 9099

#Nuevo Socket Server TCP
socketServer = socket (AF_INET,SOCK_STREAM)

#Se establece la conexion
socketServer.bind( (addSever, portSever) )
socketServer.listen()

#Ciclo en espera de peticiones
while True:
    #Se establece conexion
    socketConexion, addr = socketServer.accept()

    print("Conectado con cliente",addr)

    #Se calcula la hora de peticion
    hour = datetime.now()
    #Se convierte en cadena
    hourString = hour.strftime("%Y%m%d %H:%M:%f")
    #Enviamos hora y fecha
    print("Hora que se envio al cliente",addr)
    print(hour)
    socketConexion.send(hourString .encode())

    #Cerramos la conexion
    socketConexion.close()



