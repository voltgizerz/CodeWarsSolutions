def word_pattern(word):
    word = word.lower()
    dict = {}
    output =""
    cnt = -1
    for i in range(len(word)):
        if dict.get(word[i],None)==None:
            cnt+=1
            dict[word[i]] = str(cnt) #NOT FOUND ADD VALUE TO DICT
        output+=" "+dict.get(word[i],None)
    return ".".join(output.split())