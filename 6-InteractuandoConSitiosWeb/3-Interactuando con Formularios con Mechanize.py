import mechanize

import argparse

from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument('-b','--buscar',help='Opción a buscar')
parser = parser.parse_args()




def main():
    if parser.buscar:
        bus = mechanize.Browser() # creamos un objeto del navegador en esa variable
        #hacemos unas configuraciones para que no nos haga seguimiento el robots.txt
        bus.set_handle_robots(False)
        bus.set_handle_equiv(False)
        #configuro la cabecera
        bus.addheaders = [('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0')]
        bus.open('https://www.duckduckgo.com/') #con google me tira many requests, y me bloquea

        #for n in bus.forms():
        #    print(n) #localizamos a los formularios dispoibles
        
        #<TextControl(q=)>


        bus.select_form(nr=0) #el 0 hace referencia a la posición que tiene el TextControl de la página
        bus['q'] = parser.buscar 
        
        #enviamos esos datos
        bus.submit()
        
        #imprimimos la respuesta para ver que nos trae
        #print(bus.response().read())
        p = BeautifulSoup(bus.response().read(),'html5lib') #hacemos uso de beautifulsoup para traer mas claro los datos

        for link in p.find_all('a'):
            u= link.get('href')
            u = u.replace('/url?q=', '') #reemplazamos el primer argumento por nada asi las direcciones se muestran mejor
            print(u)

        #en consola debo ejecutar     -b hola      por ejemplo


    else:
        print('Palabra a buscar')

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
        exit()
