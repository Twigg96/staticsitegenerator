from htmlnode import LeafNode, HTMLNode, ParentNode
from split import markdown_to_blocks, text_to_textnodes
from blocks import BlockType, block_to_block_type
from textnode import text_node_to_html_node, TextType, TextNode, HTMLNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    document_children = []

    for block in blocks:
        block_children = []
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            header_block = block.split(" ")[0]
            header_count = header_block.count("#")
            header_content = block[header_count + 1 :]
            text_nodes = text_to_textnodes(header_content)
            for text_node in text_nodes:
                child = text_node_to_html_node(text_node)
                block_children.append(child)
            block_child = ParentNode(f"h{header_count}", block_children)
        elif block_type == BlockType.CODE:
            code_text = block[3:-3]
            code_text = code_text[1:]
            code_node = LeafNode("code", code_text)
            block_children.append(code_node)
            block_child = ParentNode("pre", block_children)
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            new_string = ""
            for line in lines:
                new_line = line[2:]
                new_string += new_line + "\n"
            final_string = new_string[:-1]
            text_nodes = text_to_textnodes(final_string)
            for text_node in text_nodes:
                child = text_node_to_html_node(text_node)
                block_children.append(child)
            block_child = ParentNode("blockquote", block_children)
        elif block_type == BlockType.UNORDERED_LIST:
            items = block.split("\n")
            for item in items:
                list_children = []
                list_piece = item[2:]
                text_nodes = text_to_textnodes(list_piece)
                for text_node in text_nodes:
                    final_node = text_node_to_html_node(text_node)
                    list_children.append(final_node)
                final_list = ParentNode("li", list_children)
                block_children.append(final_list)
            block_child = ParentNode("ul", block_children)
        elif block_type == BlockType.ORDERED_LIST:
            items = block.split("\n")
            for item in items:
                list_children = []
                list_piece = item.split(" ", 1)[1]
                text_nodes = text_to_textnodes(list_piece)
                for text_node in text_nodes:
                    final_node = text_node_to_html_node(text_node)
                    list_children.append(final_node)
                final_list = ParentNode("li", list_children)
                block_children.append(final_list)
            block_child = ParentNode("ol", block_children)
        else:
            block = block.replace("\n", " ")
            text_nodes = text_to_textnodes(block)
            for text_node in text_nodes:
                child = text_node_to_html_node(text_node)
                block_children.append(child)
            block_child = ParentNode("p", block_children)
        document_children.append(block_child)
    return ParentNode("div", document_children)
