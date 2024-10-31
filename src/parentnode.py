from htmlnode import HTMLNode

def class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError ("no tag supplied")
        if self.children is None:
            raise ValueError ("no children supplied")
        str2rtrn = ""
        for child in self.children:
            str2rtrn += 
