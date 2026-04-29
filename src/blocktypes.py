from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(markdown: str):
    if markdown.startswith(('###### ', '##### ', '#### ', '### ', '## ', '# ',)):
        return BlockType.HEADING
    if markdown.startswith(('```\n')) and markdown.endswith('```'):
        return BlockType.CODE
    if all(line.startswith('>') for line in markdown.split('\n')):
        return BlockType.QUOTE
    if all(line.startswith('- ') for line in markdown.split('\n')):
        return BlockType.UNORDERED_LIST
    if all(line.startswith(f'{i}. ') for i, line in enumerate(markdown.split('\n'), start=1)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH