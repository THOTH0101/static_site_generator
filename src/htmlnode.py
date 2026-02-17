class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        str = ""

        if self.props:
            for attribute in self.props:
                str += f' {attribute}="{self.props[attribute]}"'

        return str

    def __repr__(self):
        return f"<{self.tag}{self.props_to_html()}>\n\t{self.value}\n\t\t{self.children}\n</{self.tag}>"
