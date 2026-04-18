from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):

        super().__init__(tag=tag, value=value, props=props, children=None)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        html = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html
    
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, props={self.props}"