#!/usr/bin/env python

import pyscreenshot, time, os

name = "asl"
INTERVAL = 15
NEWFOLDER_THRESHOLD = 120
HOME = os.path.expanduser("~")
FOLDER = HOME+"/asl-scrots/"

if not os.path.isdir(FOLDER):
    os.makedirs(FOLDER)

def take_screenshot(file):
     img = pyscreenshot.grab()
     img.save(file)

def get_new_subfolder():
    latest = latest_folder()
    number = latest.split("-")[1]
    number = int(number)
    number += 1
    new = "asl-{}".format(str(number).zfill(4))
    return new

def latest_folder():
    asl_dirs = []
    for dir in ls_folders():
        if "asl-" in dir:
            asl_dirs.append(dir)
    asl_dirs = sorted(asl_dirs)
    try:
        return asl_dirs[-1]
    except IndexError:
        return ""

def ls_folders():
    return [f for f in os.listdir(FOLDER) if os.path.isdir(FOLDER+f)]

def ls_files(dir):
    return [f for f in os.listdir(dir) if os.path.isfile(dir+"/"+f)]

def latest_file(dir):
    asl_files = []
    for file in ls_files(dir):
        if "screenshot-" in file:
            asl_files.append(file)
    asl_files = sorted(asl_files)
    try:
        return asl_files[-1]
    except IndexError:
        return ""

def main():
    if latest_folder() == "":
        os.mkdir(FOLDER+"asl-0000")

    while True:
        time.sleep(INTERVAL)
        timestamp = int(time.time())
        if (not (latest_file(FOLDER+latest_folder()) == "")) and (timestamp - int(latest_file(FOLDER+latest_folder()).split("-")[1].split(".")[0])) >= (NEWFOLDER_THRESHOLD):
            new_folder = FOLDER+get_new_subfolder()
            os.mkdir(new_folder)
        else:
            print(FOLDER+latest_folder()+"/screenshot-"+str(timestamp)+".jpg")
            take_screenshot(FOLDER+latest_folder()+"/screenshot-"+str(timestamp)+".jpg")

