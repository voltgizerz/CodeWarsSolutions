def dig_pow(n, p):
    digits =[int(x) for x in str(n)]
    total = 0
    for i in range(len(digits)):
        total += pow(digits[i],p)
        p+=1
    for i in range(total):
        if total == n*i :
            return i
        elif n*i>total:
            return -1