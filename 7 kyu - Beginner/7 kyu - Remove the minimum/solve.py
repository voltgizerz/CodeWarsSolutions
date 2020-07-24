def remove_smallest(numbers):
    arr = [x for x in numbers]
    if arr:
        arr.remove(min(arr))
        return arr
    return []