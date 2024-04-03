from leafnode import LeafNode
from extract_markdown import *

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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
