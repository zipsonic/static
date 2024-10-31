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


