#!/usr/bin/env python3

import os, shutil
import adup

FOLDER = os.path.expanduser("~")+"/asl-scrots"
SUMMARIES = os.path.expanduser("~")+"/asl-summaries"
ARCHIVE = ""
FRAMERATE = 6
SMOOTH = True

def main():
    for sub_folder in sorted(os.listdir(FOLDER))[0:-1]: # All except last (so we dont go back to asl-0000)    
        res = (2560, 1440)
        if SMOOTH:
            tmp = adup.dup_folder(FOLDER+"/"+sub_folder+"/")
            cmd = "ffmpeg -y -threads 2 -r {} -pattern_type glob -i '{}*.jpg' -c:v libvpx-vp9 -b:v 2M -auto-alt-ref 0 -s {}x{} -an  -deinterlace {}".format(30, tmp.name+"/", res[0], res[1], SUMMARIES+"/"+sub_folder+".webm")   
        else:
            cmd = "ffmpeg -y -threads 2 -r {} -pattern_type glob -i '{}*.jpg' -c:v libvpx-vp9 -b:v 2M -auto-alt-ref 0 -s {}x{} -an  -deinterlace {}".format(FRAMERATE, FOLDER+"/"+sub_folder+"/", res[0], res[1], SUMMARIES+"/"+sub_folder+".webm")  
        print(cmd)
        os.system(cmd)
        if ARCHIVE == "":
            shutil.rmtree(FOLDER+"/"+sub_folder+"/")
            continue
        try:
            shutil.move(FOLDER+"/"+sub_folder+"/", ARCHIVE)
            print("Moved", sub_folder, "to", ARCHIVE)
        except shutil.Error:
            print("Folder Exists")
        if SMOOTH:
            tmp.cleanup()
        print("="*len(cmd))
