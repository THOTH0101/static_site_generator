import os
from file_operations import copy_contents_to_public
from textnode import TextNode


def main():
    root = os.getcwd()  # Or use a more robust pathing method
    src_dir = os.path.join(root, "static")
    dest_dir = os.path.join(root, "public")

    print("--- Starting Site Build ---")
    copy_contents_to_public(src_dir, dest_dir)
    print("--- Build Complete ---")


main()
