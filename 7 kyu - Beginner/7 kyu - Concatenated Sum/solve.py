def check_concatenated_sum(input,n):
    digits = [int(x) for x in str(abs(input))]
    sum = ""
    c = 0
    for i in range(len(digits)):
        while c<n:
            sum += str(digits[i])
            c+=1
        if i+1 ==len(digits):
            pass
        elif input>0 and n!=0:
            sum +="+"
        elif input<0 and n!=0:
            sum +="-"
        c=0
        if sum =="": sum="0"
    return True if input == eval("-"+sum) or  input== eval(sum) else False