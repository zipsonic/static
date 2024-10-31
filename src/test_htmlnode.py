import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_normalx2(self):
        node = HTMLNode(None,"Click Here!",None,{"href":"https://www.google.com","target":"_blank"})

        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")
    pass

    def test_normal(self):
        node = HTMLNode(None,"Click Here!",None,{"href":"https://www.google.com"})

        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\"")
    pass

class TestParentNode(unittest.TestCase):
    def test_normalx2(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        print (node.to_html())
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nochildren(self):
        node = ParentNode(
            "p",
            None,
        )
        with self.assertRaises(ValueError) as context:
            print (node.to_html())
        # Verify exception message
        self.assertEqual(str(context.exception), "no children supplied")


class TestLeafNode(unittest.TestCase):
    def test_normalx2(self):
        node = LeafNode("p","This is a paragraph of text")

        self.assertEqual(node.to_html(), "<p>This is a paragraph of text</p>")
    pass

    def test_normal(self):
        node = LeafNode("a","Click Here!",{"href":"https://www.google.com"})

        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click Here!</a>")
    pass

if __name__ == "__main__":
    unittest.main()