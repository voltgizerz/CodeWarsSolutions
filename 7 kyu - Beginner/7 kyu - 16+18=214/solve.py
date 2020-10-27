def add(num1, num2):
    num2 = str(num2)
    num1 = str(num1)
    if len(num1)<len(num2):
        num1 = ("0"*(len(num2)-len(num1)))+num1
    else:
        num2 = ("0"*(len(num1)-len(num2)))+num2
    text =""
    for i in range(len(num1)):
        text+= str(int(num1[i])+int(num2[i]))
    return int(text)