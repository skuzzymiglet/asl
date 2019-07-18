import os, tempfile

def dup_folder(path):
    tmp = tempfile.TemporaryDirectory()
    for i in os.listdir(path):
        for n in range(5):
            os.symlink(path+i, tmp.name+"/"+i.split(".")[0]+str(n)+"."+i.split(".")[1])
    return tmp

