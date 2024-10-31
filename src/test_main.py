import unittest

from leafnode import LeafNode
from textnode import *
from main import text_node_to_html_node


class TestTexttoHTMLNode(unittest.TestCase):
    def test_TEXT(self):
        textnode = TextNode("This is raw text",TextType.TEXT)
        convnode = text_node_to_html_node(textnode)
        leafnode = LeafNode(None,"This is raw text")

        self.assertEqual(convnode,leafnode)
    pass

    def test_LINK(self):
        textnode = TextNode("This is a link",TextType.LINK,"https://google.com")
        convnode = text_node_to_html_node(textnode)
        leafnode = LeafNode("a","This is a link",{"href":"https://google.com"})

        self.assertEqual(convnode,leafnode)
    pass

    def test_IMAGE(self):
        textnode = TextNode("This is an image",TextType.IMAGE,"/home/pic.jpg")
        convnode = text_node_to_html_node(textnode)
        leafnode = LeafNode("img","",{"src":"/home/pic.jpg","alt":"This is an image"})

        self.assertEqual(convnode,leafnode)
    pass


if __name__ == "__main__":
    unittest.main()