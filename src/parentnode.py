from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode's tag is None")

        if self.children is None:
            raise ValueError("ParentNode's children is None")

        res = '<' + self.tag + '>'

        for child in self.children:
            res += child.to_html()

        res += '</' + self.tag + '>'
        return res
