import unittest
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from util_funcs import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_code_delim(self):
        node = TextNode("This is text with a `code` block", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("code", TextType.CODE),
                TextNode(" block", TextType.PLAIN)
            ]
        )
    
    def test_bold_delim(self):
        node = TextNode("This is text with **bold** text", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.PLAIN)
            ]
        )

    def test_italic_delim(self):
        node = TextNode("This is text with _italic_ text", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.PLAIN)
            ]
        )
    
    def test_nested_delim(self):
        node = TextNode("This is a **text block _that_ contains multiple** delimiters", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.PLAIN),
                TextNode("text block _that_ contains multiple", TextType.BOLD),
                TextNode(" delimiters", TextType.PLAIN)
            ]
        )
    
    def test_starting_delim(self):
        node = TextNode("**This** block starts with a delimiter", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This", TextType.BOLD),
                TextNode(" block starts with a delimiter", TextType.PLAIN)
            ]
        )
    
    def test_ending_delim(self):
        node = TextNode("This block ends with a **delimiter**", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This block ends with a ", TextType.PLAIN),
                TextNode("delimiter", TextType.BOLD)
            ]
        )
    
    def test_multiple_delims(self):
        node = TextNode("This **block** will contain **multiple** valid delimiters", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This ", TextType.PLAIN),
                TextNode("block", TextType.BOLD),
                TextNode(" will contain ", TextType.PLAIN),
                TextNode("multiple", TextType.BOLD),
                TextNode(" valid delimiters", TextType.PLAIN)
            ]
        )
    
    def test_multiple_nodes(self):
        node1 = TextNode("This is the **first** node with **multiple** delimiters.", TextType.PLAIN)
        node2 = TextNode("This is the **second** node with a single delimiter.", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is the ", TextType.PLAIN),
                TextNode("first", TextType.BOLD),
                TextNode(" node with ", TextType.PLAIN),
                TextNode("multiple", TextType.BOLD),
                TextNode(" delimiters.", TextType.PLAIN),
                TextNode("This is the ", TextType.PLAIN),
                TextNode("second", TextType.BOLD),
                TextNode(" node with a single delimiter.", TextType.PLAIN)
            ]
        )

    def test_unclosed_delim(self):
        node = TextNode("This node **doesn't have valid markdown", TextType.PLAIN)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
        
    def test_mixed_nodes(self):
        node1 = TextNode("This has **bold** text", TextType.BOLD)
        node2 = TextNode("This has _italic_ text", TextType.PLAIN)
        node3 = TextNode("This has a `code` block", TextType.CODE)
        node_list = [node1, node2, node3]
        new_nodes = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This has **bold** text", TextType.BOLD),
                TextNode("This has ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.PLAIN),
                TextNode("This has a `code` block", TextType.CODE)
            ]
        )
    
    def test_split_image(self):
        node = TextNode(
            "This is text that contains an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text that contains an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )
    
    def test_split_images(self):
        node = TextNode(
            "This text has this ![image](https://i.imgur.com/zjjcJKZ.png) and also this ![picture](https://www.boot.dev/_nuxt/new_boots_profile.DriFHGho.webp) in it.",
            TextType.PLAIN
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This text has this ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and also this ", TextType.PLAIN),
                TextNode("picture", TextType.IMAGE, "https://www.boot.dev/_nuxt/new_boots_profile.DriFHGho.webp"),
                TextNode(" in it.", TextType.PLAIN)

            ],
            new_nodes,
        )
      
    def test_split_link(self):
        node = TextNode(
            "This text has a [link](www.google.com) in it.",
            TextType.PLAIN
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This text has a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "www.google.com"),
                TextNode(" in it.", TextType.PLAIN)
            ],
            new_nodes
        )
    
    def test_split_links(self):
        node = TextNode(
            "This string has two [link](www.google.com) in [it](https://www.boot.dev/_nuxt/new_boots_profile.DriFHGho.webp)",
            TextType.PLAIN
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This string has two ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "www.google.com"),
                TextNode(" in ", TextType.PLAIN),
                TextNode("it", TextType.LINK, "https://www.boot.dev/_nuxt/new_boots_profile.DriFHGho.webp"),
            ],
            new_nodes
        )
    

if __name__ == "__main__":
    unittest.main()