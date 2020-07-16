def anagrams(word, words):
    list =[]
    for x in words:
        if  "".join(sorted(word)) == "".join(sorted(x)):
            list.append(x)
    return list