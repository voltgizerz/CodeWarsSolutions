def persistence(n):
    cnt = 0
    while n>=10:
        m=1
        a = [int(i) for i in str(n)]
        for i in range(len(a)):
            m *=a[i]
        n = m
        cnt+=1
    return cnt