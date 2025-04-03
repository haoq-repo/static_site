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


def split_nodes_by_type(old_nodes, extract_func, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        extracted_items = extract_func(old_node.text)    

        # if there aren't any links, then just add the original
        if len(extracted_items) == 0:
            new_nodes.append(old_node)
            continue

        item_text = extracted_items[0][0]
        item_url = extracted_items[0][1]

        # For each image found in the text
        if text_type == TextType.IMAGE:
            delimiter = f"![{item_text}]({item_url})"
        else:
            delimiter = f"[{item_text}]({item_url})"

        sections = old_node.text.split(delimiter, 1)

        # first section is the text before the image
        if sections[0]:
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
        # process the image
        new_nodes.append(TextNode(item_text, text_type, item_url))
        # recursion on the second section of the text
        if sections[1]:
            new_nodes.extend(
                split_nodes_by_type(
                    [TextNode(sections[1], TextType.TEXT)],
                    extract_func,
                    text_type
                )
            )

    return new_nodes

def split_nodes_image(old_nodes):
    return split_nodes_by_type(old_nodes, extract_markdown_images, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes_by_type(old_nodes, extract_markdown_links, TextType.LINK)