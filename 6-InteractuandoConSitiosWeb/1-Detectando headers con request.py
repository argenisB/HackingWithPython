import requests 
import argparse # podemos detectar las instrucciones o argumentos que nos pasen por consola sin crear un menú

parser = argparse.ArgumentParser(description='Detector de cabeceras') #convertimos a parser a un objeto de la clase

parser.add_argument('-t ','--target', help='Objetivo') # añadimos los argumentos, una con dos opciones -t, --target, y una opción
#-t google.com  -> google.com es el target


parser = parser.parse_args() #a partir de acá terminamos de definir los argumentos y quiero q los vea el usr

def main():
    """
    Función para detectar las cabeceras http
    """

    if parser.target: # si se especifica un objetivo entra
        try:
            url = requests.get(url=parser.target) #intenta acceder a la página que te paso por target 
            #print(url.headers) #devuelve un valor con el contenido de la respuesta del sitio
            cabeceras = dict(url.headers) # convierto a diccionario la respuesta del sv
            for x in cabeceras: #recorro el dic
                print(x + ' : ' + cabeceras[x]) #cabeceras[x] es la key
        except:
            print('No me pude conectar!')
        
    else:
        print('No hay objetivo!')

if __name__ == "__main__":
    main() 

