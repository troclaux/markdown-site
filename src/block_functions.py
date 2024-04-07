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
        if block == "":
            continue
        res.append(block.strip())
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
    elif block[0].isdigit() and block[1] == ".":
        return block_type_ordered_list
    else:
        return block_type_paragraph

def convert_paragraph_block_to_htmlnode(block):
    if block_to_block_type(block) != block_type_paragraph:
        raise ValueError(f"Block is not a paragraph: {block}")
    return HTMLNode("p", block)

def convert_heading_block_to_htmlnode(block):
    if block_to_block_type(block) != block_type_heading:
        raise ValueError(f"Block is not a heading: {block}")
    level = 1
    while block[level] == "#":
        level += 1
    tag = f"h{level}"
    return HTMLNode(tag, block)

def convert_code_block_to_htmlnode(block):
    if block_to_block_type(block) != block_type_code:
        raise ValueError(f"Block is not a code block: {block}")
    code_block = HTMLNode("code", block)
    return HTMLNode("pre", children=code_block)

def convert_quote_block_to_htmlnode(block):
    if block_to_block_type(block) != block_type_quote:
        raise ValueError(f"Block is not a quote: {block}")
    return HTMLNode("blockquote", block)

def convert_unordered_list_to_htmlnode(block):
    if block_to_block_type(block) != block_type_unordered_list:
        raise ValueError(f"Block is not an unordered list: {block}")
    children = []
    for line in block.split("\n"):
        if line.startswith("- "):
            trimmed_list_item = line[2:]
            list_item = HTMLNode("li", trimmed_list_item)
            if children is None:
                children = [HTMLNode('li', list_item)]
            else:
                children.append(HTMLNode('li', list_item))
    unordered_list = HTMLNode("ul", block, children)
    return unordered_list

def convert_ordered_list_to_htmlnode(block):
    if block_to_block_type(block) != block_type_ordered_list:
        raise ValueError(f"Block is not an ordered list: {block}")
    children = []
    for line in block.split("\n"):
        if line[0].isdigit() and line[1] == ".":
            trimmed_list_item = line[2:]
            list_item = HTMLNode("li", trimmed_list_item)
            if children is None:
                children = [HTMLNode('li', list_item)]
            else:
                children.append(HTMLNode('li', list_item))
    ordered_list = ParentNode("ol", block, children)
    return ordered_list

# convert string to string
# convert blocks to block
# identify block type
# convert block to html node
# identify text types
# which function finds and converts inline markdown?
# do it before or after block conversion?

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
