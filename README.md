# asl
## The Auto Screen-lapse Tool

### Introduction

asl is a resource-inexpensive way to record your screen. It takes screenshots at intervals (`asl.py`) and uses ffmpeg to convert them into a video (`timelapse.py`), optionally archiving them

## Todo

+ Configuration in .ini format
+ Install scripts
+ Make it availablon on the PyPI
+ Cross platform - using ffmpeg bindings rather than `os.system()`
+ Tests, i.e. example pictures
+ PEP compliance, SLOC limit (for contributors)
+ Automatic archive zipping 
+ Timelapse from archive
+ Modularization
+ ffmpeg optimizations
