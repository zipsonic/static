from htmlnode import *
from inline_markdown import *
from markdown_blocks import *
from textnode import TextType

def markdown_to_html_node(markdown):
    markdownblocks = markdown_to_blocks(markdown)

    htmlnodes = []

    for block in markdownblocks:

        leafnodes = []
        blocktype = block_to_block_type(block)

        if blocktype in ["code","quote","paragraph"]:
            textnodes = text_to_textnodes(block)
            for textnode in textnodes:
                leafnodes.append(text_node_to_html_node(textnode))
        
        match blocktype:
            case "paragraph":
                htmlnodes.append(ParentNode("p",leafnodes))
            case "heading":
                headingnum = block.find(" ")
                textnodes = text_to_textnodes(block[headingnum+1:])
                for textnode in textnodes:
                    leafnodes.append(text_node_to_html_node(textnode))
                htmlnodes.append(ParentNode(f"h{headingnum}",leafnodes))
            case "code":
                codenode = ParentNode("code",leafnodes)
                htmlnodes.append(ParentNode("pre",codenode))
            case "quote":
                htmlnodes.append(ParentNode("blockquote",leafnodes))
            case "unordered_list":
                list = block.split("\n")
                listnodes = []
                for item in list:
                    tmpnodes = []
                    listparts = text_to_textnodes(item[2:])
                    for listpart in listparts:
                        tmpnodes.append(text_node_to_html_node(listpart))
                    listnodes.append(ParentNode("li",tmpnodes))
                htmlnodes.append(ParentNode("ul",listnodes))
            case "ordered_list":
                list = block.split("\n")
                listnodes = []
                for item in list:
                    tmpnodes = []
                    listparts = text_to_textnodes(item[3:])
                    for listpart in listparts:
                        tmpnodes.append(text_node_to_html_node(listpart))
                    listnodes.append(ParentNode("li",tmpnodes))
                htmlnodes.append(ParentNode("ul",listnodes))

    parentnode = ParentNode("div",htmlnodes)
    parenthtml = parentnode.to_html()
    return parentnode

def extract_title(markdown):
    linesplit = markdown.split("/n")

    for line in linesplit:
        if line.startswith("# "):
            return line[1:].strip()
    
    raise Exception ("Header not found")
