import urllib.request

def request(url):
    try:
        with urllib.request.urlopen(url) as f:
            if f.status != 200:
                return None
            return f.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(e.reason)
