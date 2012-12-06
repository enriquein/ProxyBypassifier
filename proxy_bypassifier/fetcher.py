import urllib
from urlparse import urlparse, parse_qs

def get_url_contents(url, is_google_result_url):
    stripped = url.strip()

    if (len(stripped) == 0 ):
        raise Exception('URL cannot be blank.')
        return

    if not (url.strip().startswith( ('http://', 'https://') )):
        stripped = 'http://' + stripped

    if (is_google_result_url == 'true'):
        urlparts = urlparse(stripped)
        querystring = parse_qs(urlparts.query)
        stripped = querystring['url'][0]

    tmp = urllib.urlopen(stripped)
    contents = tmp.read()
    tmp.close()
    return contents