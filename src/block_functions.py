from parentnode import ParentNode
from htmlnode import HTMLNode


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    res = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block != "":
            res.append(block.strip())
    if res[-1] == "":
        res.pop()
    return res

def block_to_block_type(block):
    if block.startswith("#"):
        return block_type_heading
    elif block.startswith("```") and block.endswith("```"):
        return block_type_code
    elif block.startswith(">"):
        return block_type_quote
    elif block.startswith("- "):
        return block_type_unordered_list
    elif block.startswith("1. "):
        return block_type_ordered_list
    else:
        return block_type_paragraph


def convert_text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        leaf_node = text_node_to_leaf_node(text_node)
        children.append(leaf_node)
    return children


def convert_paragraph_block_to_htmlnode(block):
    if block_to_block_type(block) != block_type_paragraph:
        raise ValueError(f"Block is not a paragraph: {block}")
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = convert_text_to_children(paragraph)
    return ParentNode("p", children)


def convert_heading_block_to_htmlnode(block):
    if block_to_block_type(block) != block_type_heading:
        raise ValueError(f"Block is not a heading: {block}")
    level = 1
    while block[level] == "#":
        level += 1
    tag = f"h{level}"
    heading_text = block[level + 1 :]
    children = convert_text_to_children(heading_text)
    return ParentNode(tag, children)


def convert_code_block_to_htmlnode(block):
    if block_to_block_type(block) != block_type_code:
        raise ValueError(f"Block is not a code block: {block}")
    code_block = ParentNode("code", block)
    return ParentNode("pre", children=code_block)


def convert_quote_block_to_htmlnode(block):
    if block_to_block_type(block) != block_type_quote:
        raise ValueError(f"Block is not a quote: {block}")
    lines = block.split("\n")
    joined_lines = ""
    for line in lines:
        if line[:2] == "> ":
            joined_lines += line[1:]
    # block = " ".join(lines)
    children = convert_text_to_children(joined_lines[1:])
    return ParentNode("blockquote", children)


def convert_unordered_list_to_htmlnode(block):
    if block_to_block_type(block) != block_type_unordered_list:
        raise ValueError(f"Block is not an unordered list: {block}")
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = convert_text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def convert_ordered_list_to_htmlnode(block):
    if block_to_block_type(block) != block_type_ordered_list:
        raise ValueError(f"Block is not an ordered list: {block}")
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = convert_text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    elements = '<div>'
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            children.append(convert_paragraph_block_to_htmlnode(block))
        elif block_type == block_type_heading:
            children.append(convert_heading_block_to_htmlnode(block))
        elif block_type == block_type_code:
            children.append(convert_code_block_to_htmlnode(block))
        elif block_type == block_type_quote:
            children.append(convert_quote_block_to_htmlnode(block))
        elif block_type == block_type_unordered_list:
            children.append(convert_unordered_list_to_htmlnode(block))
        elif block_type == block_type_ordered_list:
            children.append(convert_ordered_list_to_htmlnode(block))


    elements += '</div>'
    top_level_node = ParentNode('div', children)
