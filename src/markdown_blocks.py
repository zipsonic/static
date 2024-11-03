def markdown_to_blocks(markdown):
    markdownlines = markdown.split("\n")

    markdownblocks = []

    counter = 0

    while counter < len(markdownlines):

        line2add = markdownlines[counter].strip()

        if len(line2add) == 0:
            counter += 1
            continue
        if len(line2add) > 1 and line2add[0:2] == "* ":
            ismarkdownlist = True
        else:
            ismarkdownlist = False
        if ismarkdownlist and len(markdownblocks[-1]) > 1 and markdownblocks[-1][0:2] == "* ":
            line2add = markdownblocks[-1] + "\n" + line2add
            markdownblocks.pop()

        markdownblocks.append(line2add)

        counter += 1

    return markdownblocks

def block_to_block_type(markdownblock):

    strlength = len(markdownblock)

    if strlength < 1:
        raise ValueError ("nothing to parse")
    
    char2test = markdownblock[0]

    if char2test == "-":
        char2test == "*"
    
    match char2test:
        case "#":
            return "heading"
        case "`":    
            if markdownblock[0:3] == "```" and markdownblock[-3:] == "```":
                return "code"
        case ">":
            if markdownblock.count("\n") == 0 or (markdownblock.count("\n>") == markdownblock.count("\n")):
                return "quote"
        case "*":
            if markdownblock[1] == " ":
                listmarkers = markdownblock.count("\n* ") + markdownblock.count("\n- ")
                if listmarkers == 0 or (listmarkers == markdownblock.count("\n")):
                    return "unordered_list"
        case "1":
            if markdownblock[1:3] == ". ":

                if markdownblock.count("\n") == 0:
                    return "ordered_list"
                
                counter = 2

                for i in range(len(markdownblock)):
                    if markdownblock[i] == "\n":
                        if markdownblock[i+1:i+4] != (str(counter)+". "):
                            return "paragraph"
                        counter += 1
                return "ordered_list"
                
    return "paragraph"