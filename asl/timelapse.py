#! /usr/bin/env python3

import os
import shutil
import ffmpeg
from PIL import Image

FOLDER = os.path.expanduser("~")+"/asl-scrots"
SUMMARIES = os.path.expanduser("~")+"/asl-summaries"
ARCHIVE = ""
FRAMERATE = 6
SMOOTH = True
DRY = False


def start_number(d):
    return int(os.listdir(d)[0].split("-")[1].split(".")[0])


def timelapse(framerate, d, img_fmt, res, out, codec="libvpx-vp9", crf=10,
              bitrate=2500000, out_fmt="webm", threads=2):
    o = (ffmpeg
        .input(d+"screenshot-%010d."+img_fmt, pattern_type="sequence", start_number=start_number(d))
        .output("{}.{}".format(out, out_fmt),
               video_bitrate=bitrate, s="{}x{}".format(res[0], res[1]), r=framerate, crf=crf, **{"c:v": codec, "auto-alt-ref": 0})
       .overwrite_output())
    print(' '.join(o.compile()))
    if not DRY:
        o.run()


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
            timelapse(FRAMERATE, FOLDER+"/"+sub_folder+"/", "jpg", res,
                      SUMMARIES+"/"+sub_folder, crf=4)
        else:
            timelapse(FRAMERATE, FOLDER+"/"+sub_folder+"/", "jpg", res,
                      SUMMARIES+"/"+sub_folder)
        if ARCHIVE == "":
            shutil.rmtree(FOLDER+"/"+sub_folder+"/")
            continue
        try:
            shutil.move(FOLDER+"/"+sub_folder+"/", ARCHIVE)
            print("Moved", sub_folder, "to", ARCHIVE)
        except shutil.Error:
            print("Folder Exists")
