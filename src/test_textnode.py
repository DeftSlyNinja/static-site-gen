import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This should not be equal to the next node", TextType.ITALIC, "www.google.com")
        node2 = TextNode("This should not be equal to the last node", TextType.ITALIC, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_urls(self):
        node = TextNode("Link Test", TextType.LINK)
        node2 = TextNode("Link Test", TextType.LINK, "www.bootdev.com")
        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_image_node(self):
        node = TextNode("Image Test", TextType.IMAGE, "www.google.com/image")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, '')
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "www.google.com/image", "alt": "Image Test"})
    
    def test_invalid_enum(self):
        node = TextNode("This should raise an exception", "Not a valid text type")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()