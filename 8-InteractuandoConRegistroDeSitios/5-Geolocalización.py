import urllib.request as ur
import json

def main():
    """
    Determina la geolocalización de un objetivo
    """
    url = "https://ipinfo.io/216.58.222.46/json" # /ip/json
    v = ur.urlopen(url)
    j = json.loads(v.read()) #cargo ese archivo

    #recorro el diccionario
    for dato in j:
        print(dato + " : " + j[dato]) # imprimo clave valor


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')