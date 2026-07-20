from enum import Enum
from sys import prefix
from split import markdown_to_blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    is_ordered = True
    for i, line in enumerate(lines):
        prefix = f"{i+1}. "
        if not line.startswith(prefix):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
