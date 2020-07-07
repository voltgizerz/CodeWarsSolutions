def to_camel_case(text):
    return text.title().replace(text.title()[0], text[0], 1).replace("-","").replace("_","") if len(text)!=0 else ""