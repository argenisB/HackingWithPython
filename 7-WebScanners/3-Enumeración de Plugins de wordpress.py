from os import path
from progress.bar import Bar  # barra de carga de progreso
import requests


def main():
    """
    Ataque de fuerza bruta para detectar plugins en un sitio web Wordpress
    """
    if path.exists('wp-plugins.txt'):
        w = open('wp-plugins.txt','r')
        w = w.read().split('\n') #la pasamos a lista y eliminamos los saltos de linea
        lista = []
        url = '' #aquí va la url del wordpress a analizar
        b = Bar('Procesando enumeración...', max=len(w)) #barra de progreso

        for plugin in w:
            b.next() #con next le digo a bar q vaya avanzando
            try:
                p = requests.get(url=url+'/'+plugin)
                if p.status_code == 200: #significa q el plugin existe
                    final = url+'/'+plugin
                    lista.append(final.split('/')[-2]) #agrega a la lista el plugin sacando el nombre desde la derecha dos posiciones ->  wp-content/plugins/zine-press/ -> el / es el -1 el -2 el nombre del plugin
            except:
                pass
        b.finish() #terminame la barra de progreso

        for plugin in lista:
            print(f'Plugin encontrado: {plugin}')

    else:
        print('No se encuentra la lista de plugins')



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
        exit()
