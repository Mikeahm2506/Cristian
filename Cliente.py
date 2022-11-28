""""
   Algoritmo de Cristian
   Codigo Cliente
   Hernandez Martinez miguel Angel 
   Nava Manuel
"""
#librerias
from socket import*
import time
import datetime

#Se convierte la cadena en datetime
def string_time(string):
    format = '%Y%m%d %H:%M:%f'
    hourString = datetime.datetime.strptime(string,format)
    return hourString

#Cliente
ipServer = "localhost"
portServer = 9099

#Nuevo Socket Server TCP
socketClient = socket (AF_INET,SOCK_STREAM)

#Se mide el tiempo de inicio
start = time.time()
socketClient.connect((ipServer, portServer))

#Se recibe la cadena del tiempo
hourString = socketClient.recv(4096).decode()

#Se mide el tiempo final y la resta
fin = time.time()
time= fin - start

hour = string_time(hourString)

#imprimimos valores
print("Tiempo de respuesta: ", time)
middleTime = time / 2

print("Tiempo de ida: ",middleTime)

print("Hora Servidor: ",hourString)
print("Hora exacta: ", hour + datetime.timedelta(seconds=middleTime))

#Cerramos conexion
socketClient.close()

