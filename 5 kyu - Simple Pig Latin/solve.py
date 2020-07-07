def pig_it(text):
    text = text.split(" ")
    for i in range(len(text)):
        if text[i].isalpha() ==True:
            text[i]= text[i]+text[i][0]+"ay"
            text[i] = text[i][1:]
    return " ".join(text)