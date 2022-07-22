import os

ordner_list = os.listdir()
ordner_list.sort()
ordner_list.remove("rename.py")
pretext = "Die Känguru Offenbarung"

cd = 1
for ordner in ordner_list:
    if(".jpg" in ordner):
        continue
    names_list = os.listdir(ordner)
    names_list.sort()
    pos = 1
    for names in names_list:
        if(names == "position.sabp.dat"):
            continue
        if(".jpg" in names):
            continue
        print(f"{names} -> {pretext} - CD:{cd} - Pos:{pos}.mp3")
        pos += 1
    cd += 1
    print("-------------------------------------")

input("continue?")

cd = 1
for ordner in ordner_list:
    if(".jpg" in ordner):
        continue
    os.chdir(ordner)
    names_list = os.listdir()
    names_list.sort()
    pos = 1
    for names in names_list:
        if(names == "position.sabp.dat"):
            continue
        if(".jpg" in names):
            continue
        os.rename(names, f"{pretext} - CD:{cd} - Pos:{pos}.mp3")
        pos += 1
    cd += 1
    os.chdir("..")
 

