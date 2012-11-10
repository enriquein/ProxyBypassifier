import urllib

def get_url_contents(url):
    f = urllib.urlopen()
    s = f.read()
    f.close()
    return s