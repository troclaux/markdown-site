import unittest

from block_functions import *
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        input = "   This is a paragraph\n\nThis is another paragraph  \n\nThis is a third paragraph\n\n"
        expected_result = [
            "This is a paragraph",
            "This is another paragraph",
            "This is a third paragraph",
        ]
        self.assertEqual(markdown_to_blocks(input), expected_result)

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), block_type_heading)
        self.assertEqual(block_to_block_type("```code```"), block_type_code)
        self.assertEqual(block_to_block_type("> quote"), block_type_quote)
        self.assertEqual(block_to_block_type("- list"), block_type_unordered_list)
        self.assertEqual(block_to_block_type("1. list"), block_type_ordered_list)
        self.assertEqual(block_to_block_type("a paragraph"), block_type_paragraph)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs_with_inline_italic_and_code(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

        """

        node = markdown_to_html_node(md)
        print("node:", node)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()
