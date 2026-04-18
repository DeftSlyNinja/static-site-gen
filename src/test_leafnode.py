import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_no_value(self):
        node = LeafNode("h1", None)
        self.assertRaises(ValueError, node.to_html)
    
    def test_no_tag(self):
        node = LeafNode(None, "Potatoe", {"href":"www.google.com"})
        self.assertEqual(node.value, "Potatoe")
    
    def test_repr(self):
        node = LeafNode("p", "Lorem ipsum blah blah", {"href": "www.google.com", "style": "text-align:center"})
        expected = "tag=p, value=Lorem ipsum blah blah, props={'href': 'www.google.com', 'style': 'text-align:center'}"
        self.assertEqual(node.__repr__(), expected)

if __name__ == "__main__":
    unittest.main()