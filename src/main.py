from textnode import TextNode, TextType

def main():
    item = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(item)

main()