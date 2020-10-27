def capitals(word):
    return [ x for x,y in enumerate(word) if y.isupper()]