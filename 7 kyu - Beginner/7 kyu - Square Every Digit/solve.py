def square_digits(num):
    list = [ x for x in str(num)]
    for i in range(len(list)):
        list[i]= str(int(list[i])*int(list[i]))
    return int("".join(list))