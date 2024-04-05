import re


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def markdown_to_blocks(markdown):
    res = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        res.append(block.strip())
    return res
