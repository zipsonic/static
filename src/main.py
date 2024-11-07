import os
import shutil
from textnode import *
from htmlnode import *
from markdown_to_html import *

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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as file:
        file_contents = file.read()
    
    with open(template_path, 'r') as file:
        template_contents = file.read()

    dest_node = markdown_to_html_node(file_contents)

    dest = template_contents.replace("{{ Title }}",extract_title(file_contents))\
        .replace("{{ Content }}",dest_node.to_html())
    
    with open(dest_path, 'w') as file:
        file.write(dest)
    
    return

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    sourcefiles = os.listdir(dir_path_content)

    for sourcefile in sourcefiles:
        src = os.path.join(dir_path_content,sourcefile)
        if os.path.isfile(src):

            dst = os.path.join(dest_dir_path,f"{sourcefile[:-3]}.html")
            generate_page(src,template_path,dst)
        else:
            dst = os.path.join(dest_dir_path,sourcefile)
            cleandir(dst)
            generate_pages_recursive(src,"template.html",dst)
    
    return



def main ():
    # sample = TextNode("This is a text node",TextType.BOLD,"https://www.boot.dev")
    # print (sample)
    # return

    copydir("static","public")
    generate_pages_recursive("content","template.html","public")

    return

main()