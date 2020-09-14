def two_sum(numbers, target):
    dict = {}
    for i, n in enumerate(numbers):
        if target - n in dict:
            return [dict[target-n], i]
        dict[n] = i