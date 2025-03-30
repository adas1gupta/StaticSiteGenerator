class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        total = ''
        for item in self.props:
            total += f"{item}=\"{self.props[item]}\" "
        
        return total.rstrip(' ')
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise(ValueError)
        elif not self.tag:
            return self.value 
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
