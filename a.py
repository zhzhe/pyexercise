import urllib.request
import urllib.error

def download(url , num_retries = 2 ):
    print('Downloading:',url)
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError , HTTPError , ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0 :
            if hasattr(e,'code') and 500 <= e.code < 600 :
                #
                return download(url, num_retries-1)
    return html
        #return urllib.request.urlopen("https://home.firefoxchina.cn/").read()
