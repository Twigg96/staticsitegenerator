import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from split import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node3 = TextNode("Yeps", TextType.CODE_TEXT)
        node4 = TextNode("pey", TextType.ITALIC)
        self.assertNotEqual(node3, node4)

    def test_none(self):
        node5 = TextNode("Yeps", TextType.CODE_TEXT, None)
        self.assertIsNone(node5.url)

    def test_NotNone(self):
        node6 = TextNode("Yeps", TextType.CODE_TEXT, url="yep.com")
        self.assertIsNotNone(node6.url)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_text(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        assert split_nodes_delimiter([node], "`", TextType.CODE_TEXT) == [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE_TEXT),
            TextNode(" text", TextType.TEXT),
        ]

    def test_bold_split(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        assert split_nodes_delimiter([node], "**", TextType.BOLD) == [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_string(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            node,
        )


if __name__ == "__main__":
    unittest.main()
