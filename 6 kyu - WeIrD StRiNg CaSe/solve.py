def to_weird_case(string):
   list = string.split(" ")
   value = []
   for i in range(len(list)):
        temp =""
        for x in range(0,len(list[i]),1):
            if x%2==0:
               temp += list[i][x].upper()
            else:
               temp += list[i][x]
        value.append(temp)
   return " ".join(value)