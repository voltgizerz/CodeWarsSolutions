def Xbonacci(signature,n):
    max =len(signature)
    if n > max:
        list = signature
        for i in range(n-len(signature)):
            sum = 0
            j = i
            for x in range(max):
                sum+= list[j]
                j+=1
            list.append(sum)
    else:
        list = []
        for cnt in range(n):
            list.append(signature[cnt])
    return list