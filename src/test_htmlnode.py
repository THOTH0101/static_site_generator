import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_value(self):
        node = HTMLNode(
            "a",
            "Google",
            "button",
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_props_value2(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_print(self):
        node = HTMLNode("p", "This is a paragraph", "anchor")
        self.assertEqual(
            node.__repr__(), "<p>\n\tThis is a paragraph\n\t\tanchor\n</p>"
        )


if __name__ == "__main__":
    unittest.main()
