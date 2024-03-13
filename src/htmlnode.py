class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('to_html method not implemented')

    def props_to_html(self):
        if self.props is None:
            print("HTMLNode's props is None")
            return
        res = ''
        for key in self.props:
            res += key + '="' + self.props[key] + '" '
        return res[:-1]

    def __repr__(self):
        res = ''
        if self.tag:
            res += 'tag: ' + self.tag + '\n'
        if self.value:
            res += 'value: ' + self.value + '\n'
        if self.children:
            res += 'children:\n{\n'
            for child in self.children:
                res += repr(child)
            res += '}\n'
        if self.props:
            res += 'props: ' + self.props_to_html() + '\n'
        return res
