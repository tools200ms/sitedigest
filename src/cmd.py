

class Cmd:
    @staticmethod
    def parse(args):
        url = None

        for a in args:
            url = a

        return ActionParseSite(url)
class ActionPrintHelp (Cmd):
    pass

class ActionParseSite (Cmd):
    url = None
    def __init__(self, url):
        self.url = url
