import unittest
from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
