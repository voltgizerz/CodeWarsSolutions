def solution(s):
    list=[]
    for i in range(0,len(s),2):
        if len(s)%2==0:
            list.append(s[i:i+2])
        else:
            if i+1 == len(s):
                list.append(s[i:i+2]+"_")
            else:
                list.append(s[i:i+2])
    return list