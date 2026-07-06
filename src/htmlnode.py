class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is not None:
            return f"{self.props}"
        elif len(self.props) == 0:
            return ""
        return ""

    def __repr__(self):
        return f"{HTMLNODE.tag}, {HTMLNODE.value},{HTMLNODE.children},{HTMLNODE.props}"
