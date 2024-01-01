from pathlib import Path
import os
from os import listdir,scandir,walk
import shutil

def archivos_y_carpetas_dir(path):
    carpetas= []
    archivos=[]
    
    files=os.listdir(path)
    for file in files:
        if '.' in file:
            archivos.append(file)
        else:
            carpetas.append(file)
    return archivos,carpetas
#we move the file that is within the path to move to the prior folder

#path_to_move="C:\\Users\\laptop\\Downloads\\JDOWNLOADER"
#path_to_move="/home/rengtech/Downloads"
path_to_move="/home/rengtech/Jdownloader"
path_to_move=r'{}'.format(path_to_move)

#miro los archivos y carpetas de este directorio 
#si encuentro un .mp4 me lo muevo al path to move.

archivos,carpetas=archivos_y_carpetas_dir(path_to_move)

#recorremos las subcarpetas de la carpeta seleccionada
for carpeta in carpetas:
    subcarpeta=f"{path_to_move}//{carpeta}"
    archivos_temp,carpetas_temp=archivos_y_carpetas_dir(subcarpeta)
    for archivo in archivos_temp:
        if '.mp4' in archivo:
            dir_archivo=f"{subcarpeta}//{archivo}"
            Path(dir_archivo).rename(f"{path_to_move}//{archivo}")
            #ademas borro la carpeta que he movido
            shutil.rmtree(subcarpeta, ignore_errors=True)
# for carpeta in listdir(path_to_move):
# 	try:
# 		print(carpeta)
# 		a=f"{path_to_move}//{carpeta}"
# 		b=listdir(a)
# 		Path(f"{a}//{b[0]}").rename(f"{path_to_move}//{b[0]}")
# 		a=""
# 	except:
# 		print("File not found")

# 	#i remove the previous folder that should now be empty
# 	os.rmdir(path_to_move)
# #faltaria modulo que borre las carpetas luego
