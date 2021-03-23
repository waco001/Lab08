#MIDN Gorti + MIDN Wall Lab 08

'''Referenced:
- https://janakiev.com/blog/python-filesystem-analysis/ for recursive algorithm. DRY!

'''
import os
import sys
import hashlib
import time
from datetime import datetime
import json


ignore_dir = ["/usr", "/boot", "/bin", "/etc", "/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]
    

def part1(argv):
    for (dirpath, dirnames, filenames) in os.walk(argv[1], topdown=True):
        if(dirpath not in ignore_dir):
            for f in filenames:
                print(os.path.join(dirpath, f))
            for d in dirnames:
                print(os.path.join(dirpath, d))

def part2(argv):
    for (dirpath, dirnames, filenames) in os.walk(argv[1], topdown=True):
        if(dirpath not in ignore_dir):
            for f in filenames:
                result = os.path.join(dirpath, f)
                print(result)
                print(hashlib.sha256(result.encode()).hexdigest())
            for d in dirnames:
                result = os.path.join(dirpath, d)
                print(result)
                print(hashlib.sha256(result.encode()).hexdigest())

def part3(argv,outfilename):
    out = []
    for (dirpath, dirnames, filenames) in os.walk(argv[1], topdown=True):
        if(dirpath not in ignore_dir):
            for f in filenames:
                result = os.path.join(dirpath, f)
                #print(result)
                #print(hashlib.sha256(open(result,'rb').read()).hexdigest())
                nested_output(result,hashlib.sha256(open(result,'rb').read()).hexdigest())
            for d in dirnames:
                result = os.path.join(dirpath, d)
                #print(result)
                #print(hashlib.sha256(result.encode()).hexdigest())
                nested_output(result,hashlib.sha256(result.encode()).hexdigest())

if __name__ == "__main__":
    if(len(sys.argv) < 2): quit()
    outfilename = datetime.now().strftime("%H%M%S-%d%b%Y") + ".SY402Log"
    part3(sys.argv,outfilename)
    #part2(sys.argv)
    #part1(sys.argv)