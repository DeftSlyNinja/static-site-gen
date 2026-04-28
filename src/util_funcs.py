import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def markdown_to_blocks(markdown: str):
    if markdown == "":
        return [markdown]
    blocks = markdown.split('\n\n')
    final_blocks = []
    for block in blocks:
        block = block.strip()
        if block != "":
            final_blocks.append(block)
    return final_blocks