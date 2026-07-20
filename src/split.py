import re

from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    split_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            continue
        if not images:
            split_nodes.append(node)
            continue
        remaining = node.text
        for text, url in images:
            sections = remaining.split(f"![{text}]({url})", 1)
            before = sections[0]
            after = sections[1]
            if before:
                split_nodes.append(TextNode(before, TextType.TEXT))
            split_nodes.append(TextNode(text, TextType.IMAGES, url))
            remaining = after
        if remaining:
            split_nodes.append(TextNode(remaining, TextType.TEXT))
    return split_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    split_nodes = []
    for node in old_nodes:
        link = extract_markdown_links(node.text)
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            continue
        if not link:
            split_nodes.append(node)
            continue
        remaining = node.text
        for text, url in link:
            sections = remaining.split(f"[{text}]({url})", 1)
            before = sections[0]
            after = sections[1]
            if before:
                split_nodes.append(TextNode(before, TextType.TEXT))
            split_nodes.append(TextNode(text, TextType.LINKS, url))
            remaining = after
        if remaining:
            split_nodes.append(TextNode(remaining, TextType.TEXT))
    return split_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes


def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    blocks = []
    for raw_block in raw_blocks:
        lines = [line.strip() for line in raw_block.split("\n")]
        block = "\n".join(lines).strip()
        if block == "":
            continue
        blocks.append(block)
    return blocks
