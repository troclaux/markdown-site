import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):

    def test_tag(self):
        n1 = HTMLNode(tag="p", value="Text in paragraph", props={"id": "main"})
        self.assertEqual(n1.tag, 'p')

    def test_value(self):
        n1 = HTMLNode(tag="p", value="Text in paragraph", props={"id": "main"})
        self.assertEqual(n1.value, 'Text in paragraph')

    def test_children(self):
        n1 = HTMLNode(tag="p", value="Text in paragraph", props={"id": "main"})
        n2 = HTMLNode("p", "Text in paragraph", [n1], {"id": "main"})
        self.assertEqual(n1, n2.children[0])

    def test_props(self):
        n1 = HTMLNode(tag="p", value="Text in paragraph", props={"id": "main"})
        self.assertEqual(n1.props, {"id": "main"})

    def test_props_to_html(self):
        n1 = HTMLNode(tag="p", value="Text in paragraph", props={"id": "main"})
        self.assertEqual(n1.props_to_html(), 'id="main"')


if __name__ == "__main__":
    unittest.main()
