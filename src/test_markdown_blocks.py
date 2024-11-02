import unittest

from markdown_blocks import *


class Testmarkdownblocks(unittest.TestCase):


    def test_markdown_to_blocks1(self):
        testmarkdown = """# This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item"""
        
        resultblocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
            ]
        
        self.assertListEqual(markdown_to_blocks(testmarkdown),resultblocks)

    def test_markdown_to_blocks2(self):
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
        
        self.assertListEqual(markdown_to_blocks(testmarkdown),resultblocks)

if __name__ == "__main__":
    unittest.main()