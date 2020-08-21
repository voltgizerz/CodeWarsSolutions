def no_boring_zeros(n):
    return int(str(n).strip("0")) if len(str(n))>1 else n