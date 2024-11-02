import unittest

from htmlnode import *
from textnode import *
from inline_markdown import *

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        testtxt = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        testlist = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        self.assertListEqual(extract_markdown_images(testtxt),testlist)

    def test_extract_markdown_links(self):
        testtxt = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        testlist = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

        self.assertListEqual(extract_markdown_links(testtxt),testlist)

    def test_split_nodes_link(self):
        testnode = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        resultnode =  [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(split_nodes_link([testnode]),resultnode)

    def test_split_nodes_link2(self):
        testnode = TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) with text after",
            TextType.TEXT,
        )
        resultnode =  [
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode(" with text after", TextType.TEXT),
        ]
        self.assertListEqual(split_nodes_link([testnode]),resultnode)

    def test_split_nodes_image(self):
        testnode = TextNode(
            "This is text with an image ![flower](https://www.boot.dev/flower.jpg) and ![jasper](https://www.youtube.com/jasper.png)",
            TextType.TEXT,
        )
        resultnode =  [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("flower", TextType.IMAGE, "https://www.boot.dev/flower.jpg"),
            TextNode(" and ", TextType.TEXT),
            TextNode("jasper", TextType.IMAGE, "https://www.youtube.com/jasper.png"),
        ]
        self.assertListEqual(split_nodes_image([testnode]),resultnode)

    def test_split_nodes_image2(self):
        testnode = TextNode(
            "![flower](https://www.boot.dev/flower.jpg) and ![jasper](https://www.youtube.com/jasper.png) with text after",
            TextType.TEXT,
        )
        resultnode =  [
            TextNode("flower", TextType.IMAGE, "https://www.boot.dev/flower.jpg"),
            TextNode(" and ", TextType.TEXT),
            TextNode("jasper", TextType.IMAGE, "https://www.youtube.com/jasper.png"),
            TextNode(" with text after", TextType.TEXT),
        ]
        self.assertListEqual(split_nodes_image([testnode]),resultnode)

    def test_text_to_textnodes(self):
        testtext = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        resultnode =  [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_textnodes(testtext),resultnode)

    def test_markdown_to_blocks(self):
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

    def test_markdown_to_blocks(self):
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
