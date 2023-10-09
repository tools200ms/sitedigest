from html.parser import HTMLParser

class Parser(HTMLParser):
    ID_TAGS = ('p', 'title', 'a', 'li', 'th', 'td', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',
               'b', 'u', 'i', 'strong')
    # br, br, br
    def __init__(self):
        HTMLParser.__init__(self)
        self.stack = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)

    def handle_endtag(self, tag):
        self.stack.pop()

    def handle_data(self, data):

        if len(self.stack) == 0:
            return None

        trimed = data.strip()

        if len(trimed) == 0:
            return None

        path = "> "
        for t in self.stack:
            path = path + t + ", "

        print(path)
        print(self.lasttag)
        print("data: ", trimed)

        return None
