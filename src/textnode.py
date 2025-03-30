from enum import Enum 

class TextType(Enum):
    NORMAL_TEXT = 'Normal text'
    BOLD_TEXT = '**Bold text**'
    ITALIC_TEXT = '_Italic text_'
    CODE_TEXT = 'Code text'
    LINKS = '[anchor text]url'
    IMAGES = '![alt text](url)'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url 
    
    def __eq__(self, other):
        if other.text == self.text and other.text_type == self.text_type and self.url == other.url:
            return True 
        return False 
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"