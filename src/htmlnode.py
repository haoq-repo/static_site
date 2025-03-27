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