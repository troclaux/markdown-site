from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):

        if self.value is None:
            raise ValueError("leaf node's value is None")

        if self.tag is None:
            return self.value

        html_str = f'<{self.tag}'

        if self.props is not None:
            for prop_key in self.props:
                html_str += f' {prop_key}="{self.props[prop_key]}"'

        html_str += f'>{self.value}</{self.tag}>'
        return html_str
