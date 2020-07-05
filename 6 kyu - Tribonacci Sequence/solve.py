def tribonacci(signature, n):
    j = 3
    if n<3:
        if n==3:
            signature = signature
        elif n==2:
            signature.pop(2)
        elif n==1:
            signature.pop(2)
            signature.pop(1)
    else:
        for i in range(3,n):
            signature.append(signature[i-1]+signature[i-2]+signature[i-3])
    return [] if n == 0 else signature