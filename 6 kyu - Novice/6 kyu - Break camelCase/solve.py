def solution(s):
    split = [char for char in s]
    word =""
    for i in range(len(split)):
        if split[i].isupper() ==True:
           word+=" "+split[i]
        else:
           word+=split[i]
    return word