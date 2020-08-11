import requests
from bs4 import BeautifulSoup

def main():
    sitio = 'www.google.com'
    headers = {'User-Agent':'Firefox'}
    a = requests.get(f'https://viewdns.info/reverseip/?host={sitio}&t=1',headers=headers)
    b = BeautifulSoup(a.text,'html5lib')
    c= b.find(id='null') #buscamos el id null del codigo fuente que hace referencia a la tabla
    d = c.find(border='1') #ahora accedo a la otra tabla
    for link in d.find_all('tr'):
        print('Sitio web encontrado: '+link.td.string)


try:
    main()
except KeyboardInterrupt:
    print('Saliendo...')