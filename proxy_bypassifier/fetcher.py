import urllib
from urlparse import urlparse, parse_qs, urlsplit

def get_url_contents(url, is_google_result_url):
    stripped = url.strip()

    if (len(stripped) == 0 ):
        raise Exception('URL cannot be blank.')
        return

    if not (url.strip().startswith( ('http://', 'https://') )):
        stripped = 'http://' + stripped

    if (is_google_result_url):
        urlparts = urlparse(stripped)
        querystring = parse_qs(urlparts.query)
        stripped = querystring['url'][0]

    tmp = urllib.urlopen(stripped)
    contents = tmp.read()
    tmp.close()
    return contents

def get_remote_file(url):
    file_contents = get_url_contents(url, False)
    return file_contents

def get_filename_from_url(url):
    return urlsplit(url)[2].split('/')[-1]