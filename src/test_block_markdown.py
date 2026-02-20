import unittest

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading(self):
        self.assertEqual(block_to_block_type("# heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###heading"), BlockType.PARAGRAPH)

    def test_code(self):
        code = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote(self):
        quote = "> this is a quote\n> with multiple lines"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
        bad_quote = "> line 1\nline 2"
        self.assertEqual(block_to_block_type(bad_quote), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        ul = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("* item 1"), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        ol = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("2. wrong"), BlockType.PARAGRAPH)
        bad_ol = "1. first\n3. third"
        self.assertEqual(block_to_block_type(bad_ol), BlockType.PARAGRAPH)

    def test_paragraph(self):
        text = "This is just a normal paragraph of text."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
