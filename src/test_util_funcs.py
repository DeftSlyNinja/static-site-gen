import unittest
from util_funcs import extract_markdown_images, extract_markdown_links

class TestUtilFuncs(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This text has a link [to somewhere](www.somewhere.com) and so is [this](www.google.com)"
        )
        self.assertListEqual(
            [
                ("to somewhere", "www.somewhere.com"),
                ("this", "www.google.com")
            ],
            matches
        )