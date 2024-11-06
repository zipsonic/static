import unittest

from htmlnode import *
from textnode import *
from markdown_to_html import *

class Testmarkdownblocks(unittest.TestCase):
    def test_markdown_to_html(self):
        testmarkdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

*This* is another sentence at the end to test

* A single item list"""
        
        resultblocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
            "*This* is another sentence at the end to test",
            "* A single item list"
            ]
        
        self.assertEqual(markdown_to_html_node(testmarkdown),"resultblocks")



#     def test_markdown_to_html2(self):
#         testmarkdown = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        
#         resultblocks = [
#             "# This is a heading",
#             "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
#             """* This is the first list item in a list block
# * This is a list item
# * This is another list item""",
#             "*This* is another sentence at the end to test",
#             "* A single item list"
#             ]
        
#         self.assertEqual(markdown_to_html_node(testmarkdown),"resultblocks")

if __name__ == "__main__":
    unittest.main()

