def decrypt(code):
    code = code.split(" ")
    extract = []
    for i in code:
        number = [int(x) for x in i if x.isnumeric()]
        if sum(number)>26:
            extract.append(sum(number)%27)
        else:
            extract.append(sum(number))
            
    for i in range(len(extract)):
        if extract[i] == 0:
            extract[i]= " "
        else:
            extract[i]= chr(extract[i]+96)
    return "".join(extract)

#https://www.codewars.com/kata/reviews/586992f8d2ccf1df960012e5/groups/5f1acb7a354fd60001ed23fb