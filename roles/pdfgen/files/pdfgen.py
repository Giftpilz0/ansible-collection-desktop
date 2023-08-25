#!/usr/bin/python3

import time
import os
import sys
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

workDirectory = sys.argv[1]
os.chdir(workDirectory)


################################ functions
def on_modified(event):
    excactFile = event.src_path
    excactFile = excactFile[excactFile.rfind("/") + 1 :]
    directory = event.src_path
    directory = directory[: directory.rfind("/")]
    print(directory + excactFile)
    print("libreoffice --headless --convert-to pdf '" + excactFile + "'")
    os.system(
        "cd '"
        + directory
        + "' && libreoffice --headless --convert-to pdf '"
        + excactFile
        + "'"
    )


################################ eventHandler
patterns = ["*.docx", "*.odt", "*.pptx", "*.odp", "*.dotx", "*.ott", "*.potx", "*.otp"]
ignore_patterns = None
ignore_directories = True
case_sensitive = False
eventHandler = PatternMatchingEventHandler(
    patterns, ignore_patterns, ignore_directories, case_sensitive
)

################################ observer
path = "./"
recursively = True
observer = Observer()
observer.schedule(eventHandler, path, recursive=recursively)

################################ call function on handler
eventHandler.on_modified = on_modified

################################ init
observer.start()

################################ dont stop
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
