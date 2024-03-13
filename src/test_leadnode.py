
import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):

    def test_tag(self):
        n = LeafNode(tag="p", value="Text in paragraph", props={"id": "main"})
        self.assertEqual(n.tag, 'p')

    def test_value(self):
        n = LeafNode(tag="p", value="Text in paragraph", props={"id": "main"})
        self.assertEqual(n.value, 'Text in paragraph')

    def test_props(self):
        n = LeafNode(tag="p", value="Text in paragraph", props={"id": "main"})
        self.assertEqual(n.props, {"id": "main"})

    def test_props_to_html(self):
        n = LeafNode(tag="p", value="Text in paragraph", props={"id": "main"})
        n.props["href"] = "app.com"
        self.assertEqual(
            n.to_html(), '<p id="main" href="app.com">Text in paragraph</p>')

    def test_to_html_without_props(self):
        n = LeafNode(tag="p", value="Text in paragraph")
        self.assertEqual(n.to_html(), '<p>Text in paragraph</p>')


if __name__ == "__main__":
    unittest.main()
