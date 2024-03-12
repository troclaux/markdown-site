
import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is my test", "italic", "www.amazon.com")
        node2 = TextNode("This is my test", "italic", "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("Countdown: 1, 2, 3", "bold", "www.youtube.com")
        node2 = TextNode("Countdown: 1, 2, 3", "underline", "www.youtube.com")
        self.assertNotEqual(node, node2)

    def test_eq_4(self):
        node = TextNode("This is a string", "bold", "www.github.com")
        node2 = TextNode("Different string", "bold", "www.github.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
