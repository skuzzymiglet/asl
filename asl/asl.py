#!/usr/bin/env python

import pyscreenshot
import time
import os

name = "asl"
INTERVAL = 15
NEWFOLDER_THRESHOLD = 120
HOME = os.path.expanduser("~")
FOLDER = HOME+"/asl-scrots/"

if not os.path.isdir(FOLDER):
    os.makedirs(FOLDER)


def take_screenshot(f):
    img = pyscreenshot.grab()
    img.save(f)


def get_new_subfolder():
    latest = latest_folder()
    number = latest.split("-")[1]
    number = int(number)
    number += 1
    new = "asl-{}".format(str(number).zfill(4))
    return new


def latest_folder():
    asl_dirs = []
    for d in ls_folders():
        if "asl-" in d:
            asl_dirs.append(d)
    asl_dirs = sorted(asl_dirs)
    try:
        return asl_dirs[-1]
    except IndexError:
        return ""


def ls_folders():
    return [f for f in os.listdir(FOLDER) if os.path.isdir(FOLDER+f)]


def ls_files(d):
    return [f for f in os.listdir(d) if os.path.isfile(d+"/"+f)]


def latest_file(d):
    asl_files = []
    for file in ls_files(d):
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
        timestamp = int(time.time())
        folders_exist = not (latest_file(FOLDER+latest_folder()) == "")
        if folders_exist and (timestamp - int(latest_file(FOLDER+latest_folder()).split("-")[1].split(".")[0])) >= NEWFOLDER_THRESHOLD:
            new_folder = FOLDER+get_new_subfolder()
            os.mkdir(new_folder)
        else:
            name = FOLDER+latest_folder()+"/screenshot-"+str(timestamp)+".jpg"
            print(name)
            take_screenshot(name)
        time.sleep(INTERVAL)
