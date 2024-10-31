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