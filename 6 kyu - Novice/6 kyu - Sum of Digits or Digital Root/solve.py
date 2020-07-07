def digital_root(n):
    while n >= 10:
        z = 0
        sum = 0
        x = [int(i) for i in str(n)]
        while z < len(x):
            sum += x[z]
            z += 1
        n = sum
    return n