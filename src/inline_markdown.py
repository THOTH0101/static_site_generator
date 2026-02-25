import re
from block_markdown import BlockType, block_to_block_type, text_to_heading_tag
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


def create_block_nodes(text):
    block_type = block_to_block_type(text)
    children_nodes = []

    if block_type == BlockType.CODE:
        children_nodes.append(
            ParentNode("pre", [LeafNode("code", text.strip("```").lstrip("\n"))])
        )

    if block_type == BlockType.HEADING:
        sections = text.split("\n")
        for section in sections:
            if section:
                children_nodes.append(
                    ParentNode(
                        text_to_heading_tag(section),
                        text_to_children(section.split(" ", 1)[1]),
                    )
                )

    if block_type == BlockType.PARAGRAPH:
        children_nodes.append(
            ParentNode(
                "p",
                text_to_children(" ".join(text.split("\n"))),
            )
        )

    if block_type == BlockType.QUOTE:
        sections = text.split("\n")
        quote_block = " ".join(
            list(map(lambda line: line.strip(">").strip(), sections))
        )
        children_nodes.append(ParentNode("blockquote", text_to_children(quote_block)))

    if block_type == BlockType.UNORDERED_LIST:
        sections = text.split("\n")
        ul_block = []
        for section in sections:
            ul_block.append(
                ParentNode(
                    "li",
                    text_to_children(section.lstrip("- ")),
                )
            )
        children_nodes.append(ParentNode("ul", ul_block))

    if block_type == BlockType.ORDERED_LIST:
        sections = text.split("\n")
        ol_block = []
        for section in sections:
            ol_block.append(
                ParentNode(
                    "li",
                    text_to_children(section.split(". ", 1)[1]),
                )
            )
        children_nodes.append(ParentNode("ol", ol_block))

    return children_nodes


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return list(map(lambda text_node: text_node_to_html_node(text_node), text_nodes))


def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown: formatted section not closed")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_str = old_node.text
        images = extract_markdown_images(split_str)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image_alt, image_link in images:
            sections = split_str.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            split_str = sections[1]

        if split_str != "":
            new_nodes.append(TextNode(split_str, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_str = old_node.text
        links = extract_markdown_links(split_str)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link_alt, link_url in links:
            sections = split_str.split(f"[{link_alt}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            split_str = sections[1]

        if split_str != "":
            new_nodes.append(TextNode(split_str, TextType.TEXT))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
