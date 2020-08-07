import json
import urllib.request as ur
def main():
    """
    Enumeración de usuarios de un sitio web Wordpress
    """
    url_original = "https://example/wp-json/wp/v2/users" #cambiar example por el sitio a analizar
    url = ur.urlopen(url_original)
    print(f'El sitio de Wordpress a analizar es: {url_original}')
    for u in json.loads(url.read()):
        user = u['slug']
        print(f'Usuario: ', user)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
        exit()
