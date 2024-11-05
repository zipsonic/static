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

        if blocktype in ["heading","code","quote","paragraph"]:
            textnodes = text_to_textnodes(block)
            for textnode in textnodes:
                leafnodes.append(text_node_to_html_node(textnode))
        
        match blocktype:
            case "paragraph":
                htmlnodes.append(HTMLNode("p",None,leafnodes))
            case "heading":
                headingnum = block.find(" ")
                htmlnodes.append(HTMLNode(f"h{headingnum}",None,leafnodes))
            case "code":
                codenode = HTMLNode("code",None,leafnodes)
                htmlnodes.append(HTMLNode("pre",None,codenode))
            case "quote":
                htmlnodes.append(HTMLNode("blockquote",None,leafnodes))
            case "unordered_list":
                list = block.split("\n")
                listnodes = []
                for item in list:
                    tmpnodes = [LeafNode(None,item[0:2])]
                    listparts = text_to_textnodes(item[2:])
                    for listpart in listparts:
                        tmpnodes.append(text_node_to_html_node(listpart))
                    listnodes.append(HTMLNode("li",None,tmpnodes))
                htmlnodes.append(HTMLNode("ul",None,listnodes))
            case "ordered_list":
                list = block.split("\n")
                listnodes = []
                for item in list:
                    tmpnodes = [LeafNode(None,item[0:3])]
                    listparts = text_to_textnodes(item[3:])
                    for listpart in listparts:
                        tmpnodes.append(text_node_to_html_node(listpart))
                    listnodes.append(HTMLNode("li",None,tmpnodes))
                htmlnodes.append(HTMLNode("ul",None,listnodes))

    parentnode = ParentNode("div",htmlnodes)
    return parentnode