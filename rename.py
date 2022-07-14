import os

pretext = "Känguru Chroniken"
cd = input("CD: ") 
nummer = 1

orginal_names = os.listdir()

for orginal_name in orginal_names:
    if(orginal_name == 'rename.py'):
        continue
    print(f"{pretext} CD:{cd} Nr:{nummer}.mp3")
    nummer += 1


input("continue?")
nummer = 1


for orginal_name in orginal_names:
    if(orginal_name == 'rename.py'):
        continue
    os.rename(orginal_name, f"{pretext} CD:{cd} Nr:{nummer}.mp3")
    nummer += 1
