def domain_name(url):
    url = url.replace("http://","").replace("www.","").replace("https://","")
    return url[0:url.index(".")]