from html.parser import HTMLParser

class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_p = []

    def handle_starttag(self, tag, attrs):
        if (tag == 'p'):
            self.in_p.append(tag)

    def handle_endtag(self, tag):
        if (tag == 'p'):
            self.in_p.pop()

    def handle_data(self, data):
        if self.in_p:
            print("<p> data :", data)
