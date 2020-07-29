archivo = open("archivo1.txt","w") #nombre_archivo , modo (write)
nombre = input('Nombre: ')
edad = input('Edad: ')
pais = input('País: ')

archivo.write(nombre)
archivo.write("\n")
archivo.write(edad)
archivo.write("\n")
archivo.write(pais)

print("Datos escritos")
archivo.close()

    