def narcissistic( value ):
    digits = [int(x) for x in str(value)]
    check =""
    for i in range(len(digits)):
        if i!=0: check +="+"
        check += str(pow(int(digits[i]),len(digits)))
    return True if eval(check)==value else False