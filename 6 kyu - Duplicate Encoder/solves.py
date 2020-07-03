from collections import Counter
def duplicate_encode(word):
    encode = ""
    list = Counter(word.lower())
    for i in range(len(word)):
        if list[word[i].lower()]>1:
            encode +=")"
        else:
            encode +="("
    return encode