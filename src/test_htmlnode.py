import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_none(self, props=None):
        node5 = HTMLNode()
        self.assertIsNone(node5.props)

    def test_NotNone(self):
        node6 = HTMLNode(props={"href": "yep.com"})
        self.assertIsNotNone(node6.props)


if __name__ == "__main__":
    unittest.main()
