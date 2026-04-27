import unittest
from textnode import TextNode, TextType
from text_to_nodes import text_to_textnodes

class TestTextToNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This **text** contains _various_ types of `markdown` that ![need](www.google.com) to be [tested](www.boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This ", TextType.PLAIN),
                TextNode("text", TextType.BOLD),
                TextNode(" contains ", TextType.PLAIN),
                TextNode("various", TextType.ITALIC),
                TextNode(" types of ", TextType.PLAIN),
                TextNode("markdown", TextType.CODE),
                TextNode(" that ", TextType.PLAIN),
                TextNode("need", TextType.IMAGE, "www.google.com"),
                TextNode(" to be ", TextType.PLAIN),
                TextNode("tested", TextType.LINK, "www.boot.dev")
            ],
            nodes
        )