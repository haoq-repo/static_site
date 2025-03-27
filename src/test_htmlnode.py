import unittest

from htmlnode import HTMLNode

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
        
if __name__ == "__main__":
    unittest.main()