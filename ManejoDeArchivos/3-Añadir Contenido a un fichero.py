archivo = open('archivo1.txt','a') #a append

dedicacion = input('Ingrese dedicación: ')

empresa = input('Ingrese empresa: ')

idioma= input('Ingrese idioma: ')
archivo.write('\n')
archivo.write(dedicacion)
archivo.write('\n')
archivo.write(empresa)
archivo.write('\n')
archivo.write(idioma)

archivo.close()
