import os
import shutil

path= input("ENTER THE NAME OF THE DIRECTORY TO BE SORTED")
list_of_files=os.listdir(path)
print(list_of_files)

for file in list_of_files:
    name,ext=os.path.splitext(file)

    ext=ext[1:]
    if ext==" ":
        continue

    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)

    else :
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)