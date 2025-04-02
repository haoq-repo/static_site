import re

from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
    
        split_nodes = []
        sections = old_node.text.split(delimiter)
    
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
    
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    
    return new_nodes

# takes alt text and image and return tuples ie. ![rick roll](https://i.imgur.com/aKaOqIh.gif)
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    image_matches = re.findall(pattern, text)
    return image_matches

# takes links and image and return tuples ie. [to boot dev](https://www.boot.dev)
def extract_markdown_links(text):
    pattern = r"\[([^\[\]]*)\]\(([^\(\)]*)\)"
    link_matches = re.findall(pattern, text)
    return link_matches