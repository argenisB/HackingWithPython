from paquete1 import calculadora_modulo
# a diferencia de un modulo, un paquete esta compuesto por modulos y estos no se encuentran en la misma carpeta
# otra es que son reconocidos por llevar un archivo __init__.py
def main():
    while True:
        print('Bienvenido!!  \n')
        print('1.- Suma dos números')
        print('2.- Resta dos números')
        print('3.- Multiplica dos números')
        print('4.- Divide dos números')
        print('5.- Salir')

        opcion = int(input('Opción: '))

        if opcion == 1:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            calculadora_modulo.suma(num1,num2)
            
        elif opcion == 2:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            calculadora_modulo.resta(num1,num2)

        elif opcion == 3:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            calculadora_modulo.multiplicacion(num1,num2)

        elif opcion == 4:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            calculadora_modulo.division(num1,num2)    
        
        elif opcion == 5:
            exit()    

        else:
            print('\n Opción inválida !\n')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
