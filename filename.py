import os
import re

pattern = re.compile("/termo/")


current_dir = os.getcwd()
print(current_dir)

os.chdir("/Users/jmolina/Desktop/Universidad/Termodinamica /Videos")
current_dir = os.getcwd()
files = os.listdir("/Users/jmolina/Desktop/Universidad/Termodinamica /Videos")

print(" ")

j = 1

for i in range(len(files)):
    if "Clase" in files[i]: 
        j += 1

for k in range(len(files)):
    if "termodinamica" in files[k]:
        os.rename(files[k], "Clase "+ str(j) + " Termodinamica.mp4")
        j += 1

        