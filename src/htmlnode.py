class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #string
        self.value = value #string
        self.children = children #list
        self.props = props #dictionary

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
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes *must* have a value")
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"    

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children is None:
            raise ValueError("All Parent nodes *must* have children")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes *must* have a tag")
        if self.children is None:
            raise ValueError("All Parent nodes *must* have children")
        
        html_string = f"<{self.tag}{self.props_to_html()}>"
        
        for child in self.children:
            html_string += child.to_html()
        
        html_string += f"</{self.tag}>"
        
        return html_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"