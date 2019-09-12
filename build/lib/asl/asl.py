#!/usr/bin/env python

import pyscreenshot
import time
import os
import sys

if sys.platform == "win32":
   import win32gui
   import win32ui
   import win32con
   import win32api
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


def take_screenshot(f):
    if sys.platform == "win32":
        print("hi")
        hdesktop = win32gui.GetDesktopWindow()
        
        w = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        h =  win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        l =  win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        t =  win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

        desktop_dc = win32gui.GetWindowDC(hdesktop)
        img_dc = win32ui.CreateDCFromHandle(desktop_dc)
        mem_dc = img_dc.CreateCompatibleDC()

        screenshot = win32ui.CreateBitmap()
        screenshot.CreateCompatibleBitmap(img_dc, w, h)
        mem_dc.SelectObject(screenshot)

        mem_dc.BitBlt((0,0), (w,h), img_dc, (l,t), win32con.SRCCOPY)

        screenshot.SaveBitmapFile(mem_dc, f)
        mem_dc.DeleteDC()
        win32gui.DeleteObject(screenshot.GetHandle())

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
    
    print(sys.platform)
    while True:
        timestamp = int(time.time())
        folders_exist = not (latest_file(FOLDER+latest_folder()) == "")
        if folders_exist and (timestamp - int(latest_file(FOLDER+latest_folder()).split("-")[1].split(".")[0])) >= NEWFOLDER_THRESHOLD:
            new_folder = FOLDER+get_new_subfolder()
            os.mkdir(new_folder)
        name = FOLDER+latest_folder()+"/screenshot-"+str(timestamp)+".jpg"
        print(name)
        take_screenshot(name)
        time.sleep(INTERVAL)
