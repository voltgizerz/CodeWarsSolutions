def fizzbuzz(n):
    x = []
    for i in range(1,n+1):
        if i%3 == 0 and  i%5 == 0:
            x.append("FizzBuzz")
        elif i%5 == 0:
            x.append("Buzz")
        elif i%3 == 0:
            x.append("Fizz")
        else:
            x.append(i)
    return x