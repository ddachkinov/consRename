import os

def rename_files():
    flist = os.listdir(os.getcwd())
    flistC = flist[1:]
    m = 0
    for i in flistC:
        fileext = os.path.splitext(i)[1]
        os.rename(i,str(m)+fileext)
        m = m+1
rename_files()
