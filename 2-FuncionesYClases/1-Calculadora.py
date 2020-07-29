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
            suma(num1,num2)
            
        elif opcion == 2:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            resta(num1,num2)

        elif opcion == 3:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            multiplicacion(num1,num2)

        elif opcion == 4:
            num1 = int(input('Número 1: '))
            num2 = int(input('Número 2: '))
            division(num1,num2)    
        
        elif opcion == 5:
            exit()    

        else:
            print('\n Opción inválida !\n')

def suma(nro1,nro2):
    print(f'La suma da como resultado: {nro1+nro2}')

def resta(nro1,nro2):
    print(f'La resta da como resultado: {nro1-nro2}')

def multiplicacion(nro1,nro2):
    print(f'La multiplicación da como resultado: {nro1*nro2}')

def division(nro1,nro2):
    print(f'La división da como resultado: {nro1/nro2}')




if __name__ == '__main__':
    main()
