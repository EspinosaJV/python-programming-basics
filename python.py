## Utilities
# File System -- os, os.path, shutil

# os and os.path modules for interacting with the file system
# shutil can copy files

# filenames = os.listdir(dir) - the list of filenames in that directory path (not including . and ..). The filenames are just names in directory - not absolute path
# os.path.join(dir, filename) - join directory & filename to make a path
# os.path.abspath(path) - returns absolute path of given path
# os.path.dirname(path) & os.path.basename(path) - returns the dirname and the basename
# os.path.exists(path) - true or false, true if exists
# os.mkdir(dir_path) - makes one dir
# os.makedirs(dir_path) - make all needed dirs in the path
# shutil.copy(source-path, dest-path) - copy file

## Example pulls filenames from a dir, prints their relative and absolute paths
def printdir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print(filename) ## foo.txt
        print(os.path.join(dir, filename)) ## dir/foo.txt (relative to current dir)
        print(os.path.abspath(os.path.join(dir, filename))) ## /home/nick/dir/foo.txt

# Running External Processes -- subprocess
# subprocess module is a simple way to run an external command & capture the output

import subprocess

## Given a dir path, run an external 'ls -l' on it --
## shows how to call an external program
def listdir(dir):
    cmd = 'ls -l ' + dir
    print("Command to run:", cmd) ## good to debug cmd before actually running it
    (status, output) = subprocess.getstatusoutput(cmd)
    if status: ## Error case, print the command's output to stderr and exit
        sys.stderr.write(output)
        sys.exit(status)
    print(output) ## Otherwise do something witht he command's output

## Exceptions
# run-time error that halts normal execution 

try:
    ## Either of these two lines could throw an IOError, say
    ## if the file does not exist or the read() encounters a low level error.
    f = open(filename, 'rb')
    data = f.read()
    f.close()
except IOError:
    ## Control jumps directly to here if any of the above lines throws IOError.
    sys.stderr.write('problem reading:' + filename)
## In any case, the code then continues witht he line after the tyry/except

## HTTP -- urllib and urlparse
from urllib.request import urlopen

## Given a url, try to retrieve it. If it's text/html,
## print its base url and its text.
def wget(url):
    ufile = urlopen(url) ## get file-like object for url
    info = ufile.info() ## meta-info about the url content
    if info.get_content_type() == 'text/html':
        print('base url:' + ufile.geturl())
        text = ufile.read() ## read all its text
        print(text)

## Version that uses try/except to print an error message if the
## urlopen() fails.
def wget2(url):
    try:
        ufile = urlopen(url)
        if ufile.info().get_content_type() == 'text/html':
            print(ufile.read())
    except IOError:
        print('problem reading url:', url)

    