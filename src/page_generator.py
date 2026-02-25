import os
from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from markdown import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("#").strip()

    raise Exception("Invalid markdown: h1 header not found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown_content = f.read()
    html_node = markdown_to_html_node(markdown_content)
    html_str = html_node.to_html()

    with open(template_path, "r") as f:
        template_content = f.read()
    title = extract_title(markdown_content)
    gen_html = template_content.replace("{{ Title }}", title)
    full_html = gen_html.replace("{{ Content }}", html_str)

    dir_name = os.path.dirname(dest_path)
    if dir_name != "" and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(dest_path, "w") as f:
        f.write(full_html)
