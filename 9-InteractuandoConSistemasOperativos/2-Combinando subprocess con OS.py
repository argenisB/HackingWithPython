import os
import subprocess

a = open(os.devnull, 'w') #pozo sin fondo, agujero negro que lo abrimos en modo lectura
#p = subprocess.call(['ping','-c','2','1.1.1.1'],stdout=a,stderr=subprocess.STDOUT) #haga una llamada al sistema y ejecute esto -> no me va a dejar debido a los privilegios
p = subprocess.call(['ping','1.1.1.1'],stdout=a,stderr=subprocess.STDOUT) #la salida va al pozo sin fondo, al agujero negro

if p==0:
    print('El comando se ejecutó correctamente') #esto lo unico que ve el usr, ya que el comando ping va al pozo sin fondo
else:
    print('Falló la ejecución del comando')