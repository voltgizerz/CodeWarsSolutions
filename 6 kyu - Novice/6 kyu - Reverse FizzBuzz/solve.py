def reverse_fizzbuzz(string):
    if string == "Fizz":
        return [3]
    elif string =="Buzz":
        return [5]
    elif string =="Buzz Fizz":
        return [5,6]
    elif string =="Fizz Buzz":
        return [9,10]
    elif string =="FizzBuzz":
        return [15]
    string = string.split(" ")
    list=[]
    for i in range(len(string)):
        if string[i].isnumeric():
            list.extend(range(int(string[i])-i, int(string[i])-i+len(string)))
            return list