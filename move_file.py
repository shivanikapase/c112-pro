import os
import shutil

from_dir="c:/Users/SHIVANI/Downloads/c111"
to_dir="C:/Users/SHIVANI/Desktop/c112pro"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extantation=os.path.splitext(file_name)
    if extantation=='':
        continue
    if extantation in [".gif",".png",".jpg",".jpeg",".jfif"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+file_name
        path3=to_dir+"/"+file_name
        shutil.move(path1,path2,path3)
        print("move dir file")