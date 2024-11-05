import os
import shutil
from textnode import *
from htmlnode import *

def cleandir(destination):

    if os.path.exists(destination):
        shutil.rmtree(destination)

    if os.path.exists(destination):
        raise Exception (f"{destination} folder still exists")

    os.mkdir(destination)

    return

def copydir(source, destination):

    cleandir(destination)

    sourcefiles = os.listdir(source)

    for sourcefile in sourcefiles:
        src = os.path.join(source,sourcefile)
        dst = os.path.join(destination,sourcefile)
        if os.path.isfile(src):
            shutil.copy(src,dst)
        else:
            copydir(src,dst)
    return

def main ():
    # sample = TextNode("This is a text node",TextType.BOLD,"https://www.boot.dev")
    # print (sample)
    # return

    copydir("static","public")

    return

main()