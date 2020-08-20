import shutil
import sys

def main():
    if len(sys.argv) == 2: # 2 son nuestros argumentos
    # pasamos las veces que queremos que se replique nuestro archivo
        #print(sys.argv[0]+''+sys.argv[1])
        #print(sys.argv[1])
        for n in range(0, int(sys.argv[1])): #en sys.arg[1] se encuentra el nro del argumento, si le paso 4 será 4
            shutil.copy(sys.argv[0],sys.argv[0]+str(n)+'.py') #copiamos el nombre del archivo que está en la posición 0 al destino
        print(f'Se han creado {n + 1} gusanos')
    else:
        print('Argumentos necesarios.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
