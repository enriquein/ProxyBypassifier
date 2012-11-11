import urllib

def get_url_contents(url):
    stripped = url.strip()

    if (len(stripped) == 0 ):
        raise Exception('URL cannot be blank.')
        return

    if not (url.strip().startswith( ('http://', 'https://') )):
        stripped = 'http://' + stripped

    tmp = urllib.urlopen(stripped)
    contents = tmp.read()
    tmp.close()
    return contents