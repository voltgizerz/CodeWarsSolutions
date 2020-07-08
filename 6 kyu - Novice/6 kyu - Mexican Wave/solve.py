def wave(people):
    result = []
    for i in range(len(people)):
        if i ==0 and people[i]!=" ":
            result.append(people[i].upper()+people[i+1:])
        elif i!= 0 and people[i]!=" ":
            result.append(people[0:i]+people[i].upper()+people[i+1:])
    return result