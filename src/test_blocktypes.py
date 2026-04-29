import unittest
from blocktypes import BlockType, block_to_block_type

class TestBlockTypes(unittest.TestCase):
    def test_heading_to_block_type(self):
        block = "### Header with 3 #"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.HEADING)
    
    def test_code_to_block_type(self):
        block = """```
        This is a code block
        ```"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.CODE)
    
    def test_quote_to_block_type(self):
        block = ">This is a quote\n>With multiple lines\n>Three of them"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.QUOTE)
    
    def test_unordered_list_to_block_type(self):
        block = "- This is a list\n- It has several items\n- Three of them"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.UNORDERED_LIST)
    
    def test_ordered_list_to_block_type(self):
        block = "1. This is an ordered list\n2. This is an item\n3. This is another item"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.ORDERED_LIST)
    
    def test_paragraph_to_block_type(self):
        block = "This is just a block that doesn't contain anything special"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)