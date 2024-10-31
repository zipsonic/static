import unittest

from parentnode import ParentNode
from leafnode import LeafNode


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



if __name__ == "__main__":
    unittest.main()