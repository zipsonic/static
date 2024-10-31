from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

   
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.props is not None:
            preped_tag = " " + self.props_to_html()
        else:
            preped_tag = ""
        return f"<{self.tag}{preped_tag}>{self.value}</{self.tag}>"
