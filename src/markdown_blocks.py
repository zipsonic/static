def markdown_to_blocks(markdown):
    # split when there is a newline and at least another newline immediately after
    tempblocks = markdown.split("\n\n")

    # list to hold trimmed blocks
    markdownblocks = []

    #check if each block is empty, otherwise add
    for block in tempblocks:

        if block == "":
            continue
        markdownblocks.append(block.strip())

    return markdownblocks

def block_to_block_type(markdownblock):

    blocklength = len(markdownblock)

    if blocklength < 1:
        raise ValueError ("nothing to parse")
    
    if markdownblock.startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return "heading"
    
    if markdownblock[0:3] == "```" and markdownblock[-3:] == "```" and markdownblock.count("\n") > 1:
        return "code"
    
    if markdownblock[0:2] == "> " and markdownblock.count("\n> ") == markdownblock.count("\n"):
        return "quote"
    
    if markdownblock[0:2] == "* " and markdownblock.count("\n* ") == markdownblock.count("\n"):
        return "unordered_list"
    
    if markdownblock[0:2] == "- " and markdownblock.count("\n- ") == markdownblock.count("\n"):
        return "unordered_list"
    
    if markdownblock[0:3] == "1. ":

        lines = markdownblock.split("\n")
        counter = 1
        isorderedlist = True

        for line in lines:
            if not line.startswith(f"{str(counter)}. "):
                isorderedlist = False
            counter +=1
        if isorderedlist:
            return "ordered_list"
                
    return "paragraph"

