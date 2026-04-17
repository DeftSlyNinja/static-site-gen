import unittest

from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()