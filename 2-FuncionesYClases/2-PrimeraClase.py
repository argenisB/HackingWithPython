class Carro(object):
    def __init__(self,condicion):
        self.color = 'Rojo'
        self.puertas = 4
        self.tipo = 'Deportivo'
        self.condicion = condicion
    
    def movilidad(self):
        if self.condicion == True:
            print('Acelerar')
        else:
            print('Frenar')

def main():
    while True:
        #c = Carro()

        print('1.- Acelerar')
        print('2.- Frenar')
        valor = int(input('> '))

        if valor == 1:
            c = Carro(True)
            c.movilidad()
        else:
            c = Carro(False)
            c.movilidad()

if __name__ == '__main__':
    main()