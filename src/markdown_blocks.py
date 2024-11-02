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