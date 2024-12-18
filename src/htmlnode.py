class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is not None:
            rtrn_str = ""
            for item in self.props:
                if rtrn_str != "":
                    rtrn_str += " "
                rtrn_str += f"{item}=\"{self.props[item]}\""
        return rtrn_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

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

    def __eq__(self, other):
        if isinstance(other, LeafNode):
            return self.tag == other.tag and \
                self.value == other.value and \
                self.props == other.props
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

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