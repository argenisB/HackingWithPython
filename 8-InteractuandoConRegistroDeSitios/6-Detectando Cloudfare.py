import requests


def main():
    """
    Detecta el cloudfare de un sitio web
    """
    word = 'cloudflare'
    url = requests.get("") #aquí va la url del sitio a analizar
    cabeceras = dict(url.headers) #convertimos las cabeceras de la respuesta de la peticion a dicionario
    verify = False
    #print(cabeceras)
    for c in cabeceras:
        if word in cabeceras[c].lower(): #verifico si contiene el diccionario la key cloudfare
            verify = True #si está presente validamos la verificación
            break #si se rompe está presente la palabra cloudfare en la cabecera

    if verify == True:
        print('Cloudfare está presente')
    else:
        print('El sitio no tiene cloudfare')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
        exit()