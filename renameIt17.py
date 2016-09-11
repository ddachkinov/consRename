import os

def rename_files():
    file_list = os.listdir(r"F:\DEV\Python\Secret Message\alphabet")
    saved_path = os.getcwd()
    os.chdir(r"F:\DEV\Python\Secret Message\alphabet")
    file_list = saved_path[1:]
    i = 1
    for file_name in file_list:  
        preimenuvai = os.path.splitext('.jpg')[i]
        print("staro Ime - "+file_name)
        print("Novo Ime - "+file_name+str(i))
        os.rename(file_name,file_name+preimenuvai)
        i = i + 1
    os.chdir(saved_path)
rename_files()
