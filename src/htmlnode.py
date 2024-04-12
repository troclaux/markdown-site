class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        if children is not None:
            self.children = children
        else:
            self.children = []
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        res = ""
        for key in self.props:
            res += " " + key + '="' + str(self.props[key]) + '"'
        return res

    def __repr__(self):
        res = ""
        if self.tag:
            res += "tag: " + self.tag + "\n"
        if self.value:
            res += "value: " + self.value + "\n"
        if self.children:
            res += "children:\n{\n"
            for child in self.children:
                res += repr(child)
            res += "}\n"
        if self.props is not None:
            res += "props: " + self.props_to_html() + "\n"
        return res
