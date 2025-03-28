import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(
            None, 
            None, 
            None, 
            {"href": "https://www.boot.dev", "target": "_blank"}    
        )

        test_text = " href=\"https://www.boot.dev\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), test_text)

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "a", 
            "test string", 
            None,
            {"href": "https://www.boot.dev", "target": "_blank"}
        )
        
        self.assertEqual(
            "HTMLNode(a, test string, None, {'href': 'https://www.boot.dev', 'target': '_blank'})"
            , repr(node)
        )

    def test_none(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()