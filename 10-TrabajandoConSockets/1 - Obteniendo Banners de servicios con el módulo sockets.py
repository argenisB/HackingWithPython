import socket

s = socket.socket()

try:
    #s.connect(("scanme.nmap.org",22)) #hacemos una conexión a un servicio pasandole la tupla del nombre del servicio y el puerto 22 de ssh
    s.connect(("dlptest.com",21)) #el puerto 21 ftp
    banner = s.recv(1024) #la longitud del buffer es de 1024 donde guardamos el msj de bienvenida
    print(banner)
except:
    print('Ocurrió un error en la conexión')
