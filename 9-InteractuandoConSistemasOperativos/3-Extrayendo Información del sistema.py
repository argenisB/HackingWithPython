from subprocess import check_output
import subprocess

a = check_output('systeminfo',stderr=subprocess.STDOUT) #El standar error lo mando al bote de basura
#en a obtengo toda la info que me manda el comando system info
n = open('text.txt','w+') #lo abrimos en modo escritura y, si no existe que lo haga w+
n.write(a) #escribo en el txt la salida de a
print('Datos enviados a el test.txt')
n.close()

