#try:
#    while True:
#        print('Hola')
#except NameError as n:
#    print(n)
#except KeyboardInterrupt: #cntrol + c
#    print('salida forzoza')
#finally:
#    print('Se terminó la ejecución')

try:
    raise IOError #raise genera un error
except IOError:
    print('Ocurrió un error')
