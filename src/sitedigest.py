import sys
from about import *
from cmd import *
from parser import *
from request import *

print(About.getAbout())

action = Cmd.parse(sys.argv)

print("Digesting: %s" % (action.url))


resp_text = request(action.url)

if type(resp_text) != str:
    print("Non-technical issue (eg. resource is an image)")

parser = Parser()
parser.feed(resp_text)

