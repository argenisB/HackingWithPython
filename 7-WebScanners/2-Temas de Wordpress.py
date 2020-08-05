import requests
from bs4 import BeautifulSoup


def main():
    """
    Función para detectar temas de Wordpress de un sitio Wordpress
    """
    cabecera = {'User-Agent': 'Firefox'}
    url = 'https://example.com'
    peticion = requests.get(url=url, headers=cabecera)

    soup = BeautifulSoup(peticion.text, 'html5lib')

    for enlace in soup.find_all('link'):  # buscamos en todas las etiquetas links
            if '/wp-content/themes' in enlace.get('href'):
                the = enlace.get('href')
                # parseamos
                the = the.split('/')  # la hacemos lista y la separamos por /
                if 'themes' in the:  # si se encuentra themes en la lista vamos a obtener su posición
                    pos = the.index('themes')  # obtenemos la posición
                    theme = the[pos+1]  # si dejo solo posición me imprimirá themes si paso a la siguiente posicion obtengo el nombre del tema
                    print('Tema en uso: ' + theme)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
        exit()
