import sys
from file_operations import copy_contents_to_public
from page_generator import generate_pages_recursive


def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    print("base path:", base_path)
    print("--- Starting Site Build ---")
    copy_contents_to_public("./static", "./docs")
    print("--- Build Complete ---")
    generate_pages_recursive("./content", "./template.html", "./docs", base_path)
    print("--- Page Generation Complete ---")


main()
