import os

print('Ruta actual: '+ os.getcwd())

#os.chdir('C:/Users/Jarvis/Desktop') -> Nos mueve al directorio

print('Ruta actual: '+ os.getcwd())

print(os.listdir(os.getcwd())) #ls o dir de donde está el archivo actual

#os.mkdir('pruebacurso') creo una nueva carpeta

#os.rmdir('pruebacurso') remover carpeta

#os.rename('test.txt', 'test2.txt')  # renombro un archivo

os.system('ping www.google.com') #ejecuta un comando ping a google como si fuera una consola