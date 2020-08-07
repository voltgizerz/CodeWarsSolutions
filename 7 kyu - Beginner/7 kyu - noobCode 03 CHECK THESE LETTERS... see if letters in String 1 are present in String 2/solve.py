def letter_check(arr): 
    for i in (list(set(arr[1].lower()))):
        if i not in arr[0].lower():
            return False
    return True

#https://www.codewars.com/kata/reviews/5e736798c3beb800010d805e/groups/5f2abb77e568cf000170aa57