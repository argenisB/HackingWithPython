import requests
from bs4 import BeautifulSoup

def main():
    """
    Función para determinar la versión de wordpress de una página Web
    """
    url = 'https://www.example.com'
    cabecera = {'User-Agent': 'Firefox'}
    peticion = requests.get(url=url, headers=cabecera)
    # print(peticion.text)
    # filtramos los datos de la petición
    soup = BeautifulSoup(peticion.text, 'html5lib')
    try:
        for v in soup.find_all('meta'):  # generator se encuentra en la etiqueta meta
            if v.get('name') == 'generator':
                global version
                version = v.get('content')
        print('La versión de Wordpress de este sitio es: ', version)
    except:
        print('No existe Wordpress en este sitio')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
        exit()
