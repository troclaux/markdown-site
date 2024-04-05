
import unittest

from extract_markdown import *


class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        input = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        expected_result =  [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        self.assertEqual(extract_markdown_images(input), expected_result)

    def test_image_extractions_without_image(self):
        input = "This is text with no images"
        self.assertEqual(extract_markdown_images(input), [])

    def test_extract_markdown_links(self):
        input = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected_result = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(extract_markdown_links(input), expected_result)

    def test_link_extractions_without_link(self):
        input = "This is text with no links"
        self.assertEqual(extract_markdown_links(input), [])

    def test_markdown_to_blocks(self):
        input = "   This is a paragraph\n\nThis is another paragraph  \n\nThis is a third paragraph\n\n"
        expected_result = [
            "This is a paragraph",
            "This is another paragraph",
            "This is a third paragraph",
        ]
        self.assertEqual(markdown_to_blocks(input), expected_result)
