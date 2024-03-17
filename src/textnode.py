from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text != other.text:
            return False
        elif self.text_type != other.text_type:
            return False
        elif self.url != other.url:
            return False
        else:
            return True

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'


def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode('b', text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode('i', text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode('code', text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode('a', text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode('img', '', props)
    raise Exception(f"Invalid text type: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    res = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            res.append(node)
            continue

        split_text = node.text.split(delimiter)

        if (len(split_text) % 2) != 1:
            err_msg = f'{text_type} delimiter not closed ({delimiter})'
            raise Exception(err_msg)

        if len(split_text) > 1:
            for idx in range(0, len(split_text)):
                curr_text = split_text[idx]
                if (idx % 2 == 0) and (curr_text != ''):
                    res.append(TextNode(curr_text, text_type_text))
                elif (idx % 2 == 1) and (curr_text != ''):
                    res.append(TextNode(curr_text, text_type))
    return res
