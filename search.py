import os


def list_dir(dir_partent, search, path):
    try:
        os.chdir(dir_partent)
    except:
        return
    path.append(dir_partent)
    dirs = os.listdir()
    for dir in dirs:
        if(os.path.isdir(dir)):
            list_dir(dir, search, path)
        else:
            if(search in dir):
                print(dir, end="")
                print(" -> ", end="")
                for i in path:
                    print(f"{i}/", end="")
                print()
    path.pop()
    os.chdir("..")

if (__name__ == "__main__"):
    user_input = input("Suchen für: ")
    path = []
    dirs = os.listdir()
    for dir in dirs:
        if(os.path.isdir(dir)):
            list_dir(dir, user_input, path)
        else:
            print(dir)
    input("exit? ")


