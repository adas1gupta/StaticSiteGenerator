import unittest 

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        first_node = HTMLNode(None, None, None, props)
        expected_string = "href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(first_node.props_to_html(), expected_string)