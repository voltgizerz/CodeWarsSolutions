def remove_url_anchor(url):
    try:
        return url[0:url.index("#")]
    except:
        return url