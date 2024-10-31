from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError ("no tag supplied")
        if self.children is None:
            raise ValueError ("no children supplied")
        self.value = ""
        for child in self.children:
            self.value += child.to_html()
        return f"<{self.tag}>{self.value}</{self.tag}>"
        
