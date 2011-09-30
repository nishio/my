import urllib, os
import logging

def read(prefix, url, cache=None, USE_CACHE=True):
    """
    PREFIX = "http://example.com/"
    url = "some/url/to/read/index.html"
    data = read(PREFIX, url)
    """
    if not cache:
        cache = (url
                 .replace(prefix, "")
                 .replace("&", "_")
                 .replace("/", "_"))
                 
    filename = "cache/%s" % cache
    if USE_CACHE and os.path.isfile(filename):
        data = file(filename).read()
        logging.info("using cache %s", cache)
        return data
    
    logging.info("fetching form url: %s", url)
    data = urllib.urlopen(prefix + url).read()
    file(filename, "w").write(data)
    return data
