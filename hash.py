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

json_out = []
json_compare = []

def nested_output(result, hash, outfile):
    now = datetime.now().strftime("%H%M%S-%d%b%Y")

    #f = open(outfile, "a")
    #f.write(json.dumps({'filename' : result, "hash" : hash, "DT":now}))
    #print(result)
    json_out.append({'filename' : result, "hash" : hash, "datetime":now})
    #f.close()

def part1(argv):
    for (dirpath, dirnames, filenames) in os.walk(argv[2], topdown=True):
        if(dirpath not in ignore_dir):
            for f in filenames:
                print(os.path.join(dirpath, f))
            for d in dirnames:
                print(os.path.join(dirpath, d))

def part2(argv):
    for (dirpath, dirnames, filenames) in os.walk(argv[2], topdown=True):
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
    for (dirpath, dirnames, filenames) in os.walk(argv[2], topdown=True):
        if(dirpath not in ignore_dir):
            for f in filenames:
                result = os.path.join(dirpath, f)
                #print(result)
                #print(hashlib.sha256(open(result,'rb').read()).hexdigest())
                nested_output(result,hashlib.sha256(open(result,'rb').read()).hexdigest(),outfilename)
            for d in dirnames:
                result = os.path.join(dirpath, d)
                #print(result)
                #print(hashlib.sha256(result.encode()).hexdigest())
                nested_output(result,hashlib.sha256(result.encode()).hexdigest(),outfilename)
    f = open(outfilename, "w+")
    f.write(json.dumps(json_out))
    f.close()

def part4b(location):
    out = []
    for (dirpath, dirnames, filenames) in os.walk(location, topdown=True):
        if(dirpath not in ignore_dir):
            for f in filenames:
                result = os.path.join(dirpath, f)
                #print(result)
                #print(hashlib.sha256(open(result,'rb').read()).hexdigest())
                nested_output(result,hashlib.sha256(open(result,'rb').read()).hexdigest(),outfilename)
            for d in dirnames:
                result = os.path.join(dirpath, d)
                #print(result)
                #print(hashlib.sha256(result.encode()).hexdigest())
                nested_output(result,hashlib.sha256(result.encode()).hexdigest(),outfilename)
    return json_out
def part4(filein, location, filename):
    f = open(filein,"r")
    loads = f.readlines()[0]
    f.close()
    json_compare = json.loads(loads)
    json_now = part4b(location)

    files_found = []
    files_added = []
    files_deleted = []
    files_modified = []

    for i in json_compare:
        old_deleted = True
        for x in json_now:
            added = False
            if i['filename'] == x['filename']:
                if i['hash'] == x['hash']:
                    files_found.append(i['filename'])
                else:
                    files_modified.append(i['filename'])
                old_deleted = False
            else:
                added = True
            if(added):
                files_added.append(x['filename']) 
        if(old_deleted == True):
            files_deleted.append(i['filename'])

    f = open("RESULTS"+filename, 'a')
    f.write("FOUND: " + json.dumps(files_found) + "\n")
    f.write("MODIFIED: " + json.dumps(files_modified) + "\n")
    f.write("DELETED: " + json.dumps(files_deleted) + "\n")
    f.write("ADDED: " + json.dumps(files_added) +"\n")
    f.close()

    print("Found: " + str(len(files_found)) + " Old Files")
    print("Found: " + str(len(files_modified)) + " Modified Files")
    print("Found: " + str(len(files_deleted)) + " Deleted Files")
    print("Found: " + str(len(files_added)) + " New Files")
    print("These files have been logged in: " + "RESULTS"+filename + " for your records.")
        #print(i)
        #if i in json_now:
            #print(i['filename'] + " | FOUND")
        #if i not in json_now:
            #print(i['filename'] + " | DELETED")
    '''for i in json_now:
        if i not in json_compare:
            print(i["filename"] + " | CREATED")'''


if __name__ == "__main__":
    #if(len(sys.argv) < 4): quit()
    outfilename = datetime.now().strftime("%H%M%S-%d%b%Y") + ".SY402Log"
    if(sys.argv[1] == "-c"):
        part4(sys.argv[2], sys.argv[3], outfilename)
    elif(sys.argv[1] == "-s"):
        part3(sys.argv,outfilename)
    #part3(sys.argv,outfilename)
    #part2(sys.argv)
    #part1(sys.argv)