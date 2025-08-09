import os
import sys
import shutil
import time

if len(sys.argv) < 3:
    print("give source and destination")
    quit()

fromfolder = sys.argv[1]
tofolder = sys.argv[2]

if not os.path.exists(fromfolder):
    print("no source folder")
    quit()
if not os.path.exists(tofolder):
    print("no destination folder")
    quit()

files = os.listdir(fromfolder)

for f in files:
    fp = fromfolder + "/" + f
    if os.path.isfile(fp):
        newname = f
        if os.path.exists(tofolder + "/" + f):
            newname = f.split(".")[0] + "_" + str(int(time.time())) + "." + f.split(".")[1]
        shutil.copy(fp, tofolder + "/" + newname)
        print("moved", f)
