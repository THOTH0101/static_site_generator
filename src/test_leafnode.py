import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_no_tag(self):
        node = LeafNode("", "This is a plain text")
        self.assertEqual(node.to_html(), "This is a plain text")

    def test_leaf_with_no_value(self):
        node = LeafNode("a", "")
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "All leaf nodes must have a value")


if __name__ == "__main__":
    unittest.main()
