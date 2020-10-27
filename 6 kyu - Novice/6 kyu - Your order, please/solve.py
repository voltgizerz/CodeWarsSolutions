import re
def order(sentence):
    list = sentence.split(" ")
    solve =[]
    order=re.findall('\d+', sentence)
    for i in range(len(list)):
        for x in range(len(order)):
            if int(order[x])-1==i:
                solve.append(list[x])
    return " ".join(solve)