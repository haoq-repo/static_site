from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    block = block.strip()

    if re.match(r"^#{1,6} ", block):
        block_type = BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        block_type = BlockType.CODE
    elif all(line.startswith(">") for line in block.split("\n")):
        block_type = BlockType.QUOTE
    elif all(line.startswith("- ") for line in block.split("\n")):
        block_type = BlockType.ULIST
    elif all(re.match(r"^[0-9]\. ", line) for line in block.split("\n")):
        block_type = BlockType.OLIST
    else:
        block_type = BlockType.PARAGRAPH
    return block_type
