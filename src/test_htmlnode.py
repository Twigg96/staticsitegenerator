import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node5 = HTMLNode(props=None)
        self.assertIsNone(node5.props)

    def test_NotNone(self):
        node6 = HTMLNode(props={"href": "yep.com"})
        self.assertIsNotNone(node6.props)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_props(self):
        node = LeafNode("a", "yeps", {"href": "yeps.com"})
        self.assertEqual(node.to_html(), '<a href="yeps.com">yeps</a>')

    def test_leaf_no_tag(self):
        node = LeafNode(None, "yep")
        self.assertEqual(node.to_html(), "yep")

    def test_leaf_value(self):
        node = LeafNode("p", value=None)
        with self.assertRaises(ValueError):
            (node.to_html())


if __name__ == "__main__":
    unittest.main()
