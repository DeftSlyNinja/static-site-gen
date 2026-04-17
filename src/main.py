from textnode import TextNode, TextType

def main():
    newNode = TextNode("this is some text", TextType.LINK, "https://www.bootdev.com")
    print(newNode)

if __name__ == "__main__":
    main()