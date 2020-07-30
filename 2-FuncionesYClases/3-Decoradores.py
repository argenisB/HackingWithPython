#classmethod
#staticmethod
#property

class prueba1(object):
    def __init__(self,radio):
        self.radio = radio
    
    @classmethod #es un decorador que permite a la funcion indicada sin que este esté antes convertida en un objeto, si lo comento no me deja llamarlo sin instanciar prueba1
    def saludo(cls, nombre):
        print(f'Hola {nombre}')

    @staticmethod #este decorador nos permite usar una funcion dentro de una clase sin q esta reciba argumentos
    def saludo_static(): 
        print('Bienvenido') # se va a ejecutar cuando lo llamen sin pasarle argumentos a la función debido a que es un methodo statico
    
    
    @property
    def area_circulo(self):
        return 3.1416*(self.radio**2)
def main():
    #nombre = input('Ingrese nombre: ')
    #prueba1.saludo(nombre) # no tengo que hacer una instancia de prueba1 para poder acceder a este metodo
    
    #c = prueba1()
    #c.saludo_static() 

    c = prueba1(5) #le mando al init
    area = c.area_circulo
    print(area)
   
if __name__=='__main__':
    main()
