import unittest

from page_generator import extract_title


class TestPageGenerator(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is heading one h1
### This is another heading h3


and this is the first paragraph
"""
        heading_content = extract_title(md)
        self.assertEqual(heading_content, "This is heading one h1")


if __name__ == "__main__":
    unittest.main()
