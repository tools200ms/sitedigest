import urllib.request

def request(url):
    with urllib.request.urlopen(url) as f:
        print(f.read())

