def super_size(n):
    digits = [str(x) for x in str(n)]
    digits.sort(reverse=True)
    return int("".join(digits)) 