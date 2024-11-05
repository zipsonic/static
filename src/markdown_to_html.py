from htmlnode import *
from inline_markdown import *
from markdown_blocks import *

def markdown_to_html_node(markdown):
    markdownblocks = markdown_to_blocks(markdown)

    for block in markdown_to_blocks:
        blocktype = block_to_block_type(block)
        