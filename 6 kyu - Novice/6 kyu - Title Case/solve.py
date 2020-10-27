def title_case(title, minor_words=''):
    if title:
        title = title.title()
        minor_words = minor_words.title().split(" ")
        for i in minor_words:
            if i in minor_words:
                title =title.replace(i,i.lower())
        return title[0].upper()+title[1:]
    return ''