from enum import Enum
from logging import raiseExceptions
from htmlnode import LeafNode, HTMLNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE_TEXT = "code text"
    LINKS = "links"
    IMAGES = "images"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text, None)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, None)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, None)
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode("code", text_node.text, None)
    elif text_node.text_type == TextType.LINKS:
        full_url = {"href": text_node.url}
        return LeafNode("a", text_node.text, full_url)
    elif text_node.text_type == TextType.IMAGES:
        img_text = {"src": text_node.url, "alt": text_node.text}
        return LeafNode("img", "", img_text)
    else:
        raise ValueError(f"Invalid text type {text_node.text_type}")
