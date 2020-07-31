import modulo_calculadora as calculadora

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
            calculadora.suma(num1,num2)
            
        elif opcion == 2:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            calculadora.resta(num1,num2)

        elif opcion == 3:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            calculadora.multiplicacion(num1,num2)

        elif opcion == 4:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            calculadora.division(num1,num2)    
        
        elif opcion == 5:
            exit()    

        else:
            print('\n Opción inválida !\n')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
