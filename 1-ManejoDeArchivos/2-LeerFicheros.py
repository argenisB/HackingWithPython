archivo = open("wordlist.lst", "r")

#for l in archivo.read().split('\n'): #con split separo las cadenas de texto de acuerdo al salto de linea
    #print(l)
lista = archivo.read().split('\n')
print(len(lista))

for n in lista:
    print(n)