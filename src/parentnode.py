from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag value is missing")

        if not self.children:
            raise ValueError("Children node is missing")

        str_rep = f"<{self.tag}>"

        # perform recursive call on nested children
        for child in self.children:
            str_rep += child.to_html()

        str_rep += f"</{self.tag}>"
        return str_rep
