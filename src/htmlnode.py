class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        html_text = ""
        if self.props: # Check if props exists and isn't None
            for key, value in self.props.items():
                html_text += f" {key}=\"{value}\""

        return html_text

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, attributes=None):
        super().__init__(tag, value, None, attributes)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes *must* have a value")
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"    

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
