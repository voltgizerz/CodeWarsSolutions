def high_and_low(numbers):
    numInt =  [int(i) for i in numbers.split(" ")] 
    return f"{max(numInt)} {min(numInt)}"