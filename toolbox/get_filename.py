#!/usr/bin/python 
import os
import os.path

rootdir="/Users/ruqin/harbor"


for parent,dirnames,filenames in os.walk(rootdir):
    print "dirnames====="
    print dirnames
    for filename in filenames:
        print  filename
            