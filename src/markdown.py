from block_markdown import markdown_to_blocks

from htmlnode import ParentNode
from inline_markdown import create_block_nodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_nodes.extend(create_block_nodes(block))

    return ParentNode("div", html_nodes)
