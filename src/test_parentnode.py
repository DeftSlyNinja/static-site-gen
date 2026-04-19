import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_nested_children(self):
        grand_child = LeafNode("p", "I am a grandchild", {"href":"www.google.com", "style": "text-align:center"})
        child = ParentNode("div", [grand_child])
        parent = ParentNode("body", [child])
        self.assertEqual(parent.to_html(), "<body><div><p href=\"www.google.com\" style=\"text-align:center\">I am a grandchild</p></div></body>")
    
    def test_to_html_many_children(self):
        main_node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text again"),
            ],
        )
        self.assertEqual(
            main_node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>Italic text</i>Normal text again</h2>"    
        )

if __name__ == "__main__":
    unittest.main()