# !/usr/bin/env python3

import os
import sys
import shutil
import tempfile
import ffmpeg
from PIL import Image

FOLDER = os.path.expanduser("~")+"/asl-scrots"
SUMMARIES = os.path.expanduser("~")+"/asl-summaries"
ARCHIVE = ""
FRAMERATE = 6
SMOOTH = True


def dup_folder(path):
    tmp = tempfile.TemporaryDirectory()
    for i in os.listdir(path):
        for n in range(5):
            target = path+i
            f = tmp.name+"/"+i.split(".")[0]+str(n)+"."+i.split(".")[1]
            if sys.platform == "win32":
                shutil.copy(target, f)  # Copy files because symlink doesn't work
            else:
                os.symlink(target, f)
    return tmp


def timelapse(framerate, d, img_fmt, res, out, codec="libvpx-vp9",
              bitrate=2000, out_fmt="webm", threads=2):
    (ffmpeg
        .input(d+"screenshot-*."+img_fmt, pattern_type="glob")
        .output("{}.{}".format(out, out_fmt),
                video_bitrate=bitrate, s="{}x{}".format(res[0], res[1]),
                r=framerate, **{"c:v": codec, "auto-alt-ref": 0})
        .overwrite_output()
        .run())


def folder_max_res(folder):
    res = []
    for f in os.listdir(folder):
        res.append(Image.open(folder+f).size)
    return max(res)


def main():
    # All folders are timelapsed except the last (so numbering doesn't reset)
    for sub_folder in sorted(os.listdir(FOLDER))[0:-1]:
        res = folder_max_res(FOLDER+"/"+sub_folder+"/")
        if SMOOTH:
            tmp = dup_folder(FOLDER+"/"+sub_folder+"/")
            timelapse(30, tmp.name+"/", "jpg", res, SUMMARIES+"/"+sub_folder)
        else:
            timelapse(FRAMERATE, FOLDER+"/"+sub_folder+"/", "jpg", res, SUMMARIES+"/"+sub_folder)
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
