def iq_test(numbers):
    numbers = numbers.split(" ")
    even = list(filter(lambda x: (int(x) % 2 == 0), numbers))
    odd  = list(filter(lambda x: (int(x) % 2 == 1), numbers) )
    return (numbers.index(even[0])+1) if len(even)==1 else (numbers.index(odd[0])+1)
 
