import os 

def rename_files():
    file_list = os.listdir(r"/home/prantoran/cpdf") # r = use raw filepath
    print(file_list)

    saved_path = os.getcwd()
    print("Current working dir is " + saved_path)

    os.chdir(r"/home/prantoran/cpdf")


    for fn in file_list:
        print("old name:" + fn)
        print("new name:" + fn.translate("-"))
        os.rename(fn, fn.translate("-"))

    os.chdir(saved_path)

rename_files()