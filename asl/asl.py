#!/usr/bin/env python

import pyscreenshot
import time
import os
import os.path
import sys

if sys.platform == "win32":
    import pyautogui
    from ctypes import windll

    user32 = windll.user32
    user32.SetProcessDPIAware()

name = "asl"
INTERVAL = 15
NEWFOLDER_THRESHOLD = 120
HOME = os.path.expanduser("~")
FOLDER = HOME+"/asl-scrots/"

if not os.path.isdir(FOLDER):
    os.makedirs(FOLDER)


def last_modified(f):
    return int(os.path.getmtime(f))


def take_screenshot(f):
    if sys.platform == "win32":
        pyautogui.screenshot(f)
    else:
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
    asl_dirs = sorted([d for d in ls_folders() if "asl-" in d])
    try:
        return asl_dirs[-1]
    except IndexError:
        return ""


def ls_folders():
    return [f for f in os.listdir(FOLDER) if os.path.isdir(FOLDER+f)]


def ls_files(d):
    return [f for f in os.listdir(d) if os.path.isfile(d+"/"+f)]


def latest_file(d):
    asl_files = sorted([f for f in ls_files(d) if "screenshot-" in f])
    try:
        return asl_files[-1]
    except IndexError:
        return ""


def main():
    if latest_folder() == "":
        os.mkdir(FOLDER+"asl-0000")
    i = 0
    while True:
        timestamp = int(time.time())
        folders_exist = not (latest_file(FOLDER+latest_folder()) == "")
        if folders_exist and (timestamp - last_modified(FOLDER+latest_folder()+"/"+latest_file(FOLDER+latest_folder()))) >= NEWFOLDER_THRESHOLD:
            new_folder = FOLDER+get_new_subfolder()
            os.mkdir(new_folder)
        name = FOLDER+latest_folder()+"/screenshot-"+str(i).zfill(10)+".jpg"
        print(name)
        take_screenshot(name)
        i += 1
        time.sleep(INTERVAL)
