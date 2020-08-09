# pip install python-whois
import whois

dominio = input('Ingrese el nombre de dominio a buscar: ')
w = whois.whois(dominio)
print(w)
