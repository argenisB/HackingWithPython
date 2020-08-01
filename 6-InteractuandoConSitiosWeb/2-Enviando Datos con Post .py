import requests 
import argparse 
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file',help='Indica el archivo a subir') # -f archivo_a_enviar

parser = parser.parse_args() #convertimos a funcion

def main():
    """
    Función para enviar un archivo con Post
    """
    if parser.file: #si recibo como argumento un archivo...
        if path.exists(parser.file): #verificamos que exista el archivo
            archivo = open(parser.file,'rb') # lo abrimos en formato binario                                        #uploaded_file es el name del formulario
            headers = {'User-Agent':'Firefox'}
            peticion = requests.post(url='https://curso-python-0-pruebas-pentest-dvwa.000webhostapp.com/index.php',files={'uploaded_file':archivo},headers=headers)
            if parser.file in peticion.text: # si en la respuesta viene el nombre del archivo, se subió correctamente
                #print(peticion.text)
                print('Archivo subido con éxito')
            else:
                print('Falló la subida del archivo!')
        else:
            print('No existe el archivo')
    else:
        print('Necesito un archivo para subir.')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
