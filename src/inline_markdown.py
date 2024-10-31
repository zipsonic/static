from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes is None:
        raise ValueError ("no nodes to parse")
    
    split_list = []

    for node in old_nodes:

        sliced_string = node.text.split(delimiter)

        if len(sliced_string) == 1:
            split_list.append(TextNode(node,TextType.TEXT))
        elif len(sliced_string) == 2:
            raise Exception ("invalid delimiter sequence")
        else:
            if sliced_string[0] == "":
                split_list.append(TextNode(sliced_string[1], text_type))
                split_list.append(TextNode(sliced_string[2],TextType.TEXT))
            elif sliced_string[2] == "":
                split_list.append(TextNode(sliced_string[0],TextType.TEXT))
                split_list.append(TextNode(sliced_string[1], text_type))
            else:
                split_list.append(TextNode(sliced_string[0],TextType.TEXT))
                split_list.append(TextNode(sliced_string[1], text_type))
                split_list.append(TextNode(sliced_string[2],TextType.TEXT))
    
    return split_list


