# Duplicates files 5 times ech into symlinks in  a tmp

import os, tempfile, signal

def dup_folder(path):
    tmp = tempfile.TemporaryDirectory()
    for i in os.listdir(path):
        for n in range(5):
            #print(tmp.name+"/"+i.split(".")[0]+str(n)+"."+i.split(".")[1])
            os.symlink(path+i, tmp.name+"/"+i.split(".")[0]+str(n)+"."+i.split(".")[1])
    #print(os.listdir(tmp.name))
    return tmp


#def test():
 #   tmp = dup_folder("/home/skuzzyneon/asl-scrots/asl-0185")
  #  os.listdir(tmp.name)

#test()
