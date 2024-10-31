import unittest

from leafnode import LeafNode


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