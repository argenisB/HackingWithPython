import dns.resolver
from progress.bar import Bar
from os import path


def main():
    if path.exists('subdominios.txt'):
        wordlist = open('subdominios.txt','r')
        wordlist = wordlist.read().split('\n')
        lista = []
        url = 'uncaus.edu.ar'
        b = Bar('Procesando enumeración...', max=len(wordlist))
        for s in wordlist:
            b.next()
            try:
                a = dns.resolver.resolve(f'{s}.{url}','A') #Si se puede resolver esa direccion del host significa que existe
                lista.append(f'{s}.{url}')
            except:
                pass
        b.finish()
        if len(lista) > 0:
            print(f'Número de subdominios posibles: {len(lista)}')
            for e in lista:
                print(e)
        else: #si no se ha añadido ningun elemento a la lista no se pudo resolver
            print('No se encontraron subdominios')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
        exit()
