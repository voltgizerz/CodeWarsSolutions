from collections import Counter
def get_strings(city):
    char = []
    for i in city.lower():
        if i!=" " and i not in char:
            char.append(i)
    dict = Counter(city.lower())
    for i in range(len(char)):
        cnt = 0
        con = ""
        star = dict.get(char[i])
        while cnt<star:
            con+="*" 
            cnt+=1
        char[i] = char[i]+":"+con
    return ",".join(char)