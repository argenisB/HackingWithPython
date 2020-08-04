from Wappalyzer import Wappalyzer, WebPage


def main():
    wap = Wappalyzer.latest()
    try:
        web =  WebPage.new_from_url('https://www.example.com')
        tecnologias = wap.analyze(web) #este es un tipo de dato de lista

        for t in tecnologias:
            print(f'Tecnología detectada: {t}')
    except:
        print('Ha ocurrido un error!')


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo...')
        exit()