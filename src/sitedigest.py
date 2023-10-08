import sys
from about import *
from cmd import *
from parser import *
from request import *

print(About.getAbout())

action = Cmd.parse(sys.argv)

print(action.url)

parser = Parser()
parser.feed("<html><body><p>test</p></body></html>")

request(action.url)
