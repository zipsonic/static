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

    def test_block_to_block_type_heading(self):

        testmarkdown = "# this is a heading"

        self.assertEqual(block_to_block_type(testmarkdown),"heading")

    def test_block_to_block_type_code(self):

        testmarkdown = "```This is a code block```"

        self.assertEqual(block_to_block_type(testmarkdown),"code")

    def test_block_to_block_type_quote(self):

        testmarkdown = """> This is a quote block
> This is the next line in the quote block
> And 3rd line"""

        self.assertEqual(block_to_block_type(testmarkdown),"quote")
    
    def test_block_to_block_type_unorderedlist(self):

        testmarkdown = """* This is a list block
- This is the next line in the list block
- And 3rd line"""

        self.assertEqual(block_to_block_type(testmarkdown),"unordered_list")
        

    def test_block_to_block_type_orderedlist(self):

        testmarkdown = """1. This is a list block
2. This is the next line in the list block
3. And 3rd line"""

        self.assertEqual(block_to_block_type(testmarkdown),"ordered_list")
        

if __name__ == "__main__":
    unittest.main()