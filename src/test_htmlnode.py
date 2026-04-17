import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode("p", "This is a paragraph", ["ul", "text"], {"href": "www.google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), f" href=\"www.google.com\" target=\"_blank\"")

    def test_empty(self):
        node1 = HTMLNode()
        self.assertEqual(node1.tag, None)
        self.assertEqual(node1.value, None)
        self.assertEqual(node1.children, None)
        self.assertEqual(node1.props, None)
    
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()