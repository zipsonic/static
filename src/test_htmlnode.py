import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_normalx2(self):
        node = HTMLNode(None,"Click Here!",None,{"href":"https://www.google.com","target":"_blank"})

        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")
    pass

    def test_normal(self):
        node = HTMLNode(None,"Click Here!",None,{"href":"https://www.google.com"})

        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\"")
    pass


if __name__ == "__main__":
    unittest.main()