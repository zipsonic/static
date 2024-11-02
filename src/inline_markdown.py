import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes is None:
        raise ValueError ("no nodes to parse")
    
    split_list = []

    for node in old_nodes:

        sliced_string = node.text.split(delimiter)

        if len(sliced_string) == 1:
            split_list.append(node)
        elif len(sliced_string) % 2 == 0:
            raise Exception ("invalid delimiter sequence")
        else:
            for i in range(len(sliced_string)):

                if sliced_string[i] == "":
                    continue
                
                if i % 2 == 0:
                    split_list.append(TextNode(sliced_string[i],TextType.TEXT))
                else:
                    split_list.append(TextNode(sliced_string[i], text_type))
    
    return split_list

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_link(old_nodes):
    return split_nodes_link_or_image(old_nodes,True)

def split_nodes_image(old_nodes):
    return split_nodes_link_or_image(old_nodes,False)

def split_nodes_link_or_image(old_nodes,islink):
    if old_nodes is None:
        raise ValueError ("no nodes to parse")
    
    split_list = []

    for node in old_nodes:

        if islink:
            linksfound = extract_markdown_links(node.text)
            markdowntype = TextType.LINK
            del_buffer = 1
        else:
            linksfound = extract_markdown_images(node.text)
            markdowntype = TextType.IMAGE
            del_buffer = 2

        if len(linksfound) == 0:
            split_list.append(node)
        else:
            str2parse = node.text

            for i in range(len(linksfound)):
                first_instance = str2parse.find(linksfound[i][0])
                if first_instance > del_buffer:
                    split_list.append(TextNode(str2parse[:first_instance-del_buffer],TextType.TEXT))

                split_list.append(TextNode(linksfound[i][0],markdowntype,linksfound[i][1]))

                end_sequence = str2parse.find(linksfound[i][1]) + len(linksfound[i][1]) + 1
                str2parse = str2parse[end_sequence:]

            if len(str2parse) > 0:
                split_list.append(TextNode(str2parse,TextType.TEXT))

    return split_list

def text_to_textnodes(text):
    node = TextNode(text,TextType.TEXT)
    nodes = [node]
    nodes = split_nodes_delimiter(nodes,"**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"*",TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`",TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes

def markdown_to_blocks(markdown):
    markdownlines = markdown.split("\n")

    markdownblocks = []

    counter = 0

    while counter < len(markdownlines):

        line2add = markdownlines[counter].strip()

        if len(markdownlines[counter]) == 0:
            counter += 1
            continue
        if line2add[0] == "*" and (line2add.count("*") % 2 == 1):
            ismarkdownlist = True
        else:
            ismarkdownlist = False
        if ismarkdownlist and markdownblocks[-1][0] == "*":
            line2add = markdownblocks[-1] + "\n" + line2add
            markdownblocks.pop()

        markdownblocks.append(line2add)

        counter += 1

    return markdownblocks


