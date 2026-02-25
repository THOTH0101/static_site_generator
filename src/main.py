import os
from file_operations import copy_contents_to_public
from page_generator import generate_pages_recursive


def main():
    root = os.getcwd()  # Or use a more robust pathing method
    src_dir = os.path.join(root, "static")
    dest_dir = os.path.join(root, "public")

    print("--- Starting Site Build ---")
    copy_contents_to_public(src_dir, dest_dir)
    print("--- Build Complete ---")
    generate_pages_recursive("./content", "./template.html", "./public")
    print("--- Page Generation Complete ---")


main()
