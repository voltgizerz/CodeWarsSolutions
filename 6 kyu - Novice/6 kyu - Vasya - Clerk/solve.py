#https://www.codewars.com/kata/reviews/55589d81abe7a58e08000060/groups/5f1abe1659b8bf0001fc100c
def tickets(people):
    bal = {25 : 0, 50 : 0, 100 : 0} #MY MONEY
    for i in people:
        if i==25:
            bal[25]+=1
        elif i==50:
            if bal.get(25)!=0: #CHECK IF HAVE 25 dollars
                bal[25]-=1 
                bal[i]+=1
            else:
                return "NO"
        elif i==100:
            if bal.get(50)!=0 and bal.get(25)!=0: #CHECK IF HAVE 25 dollars + 50 dollars
                bal[25]-=1
                bal[50]-=1
                bal[i]+=1
            elif bal.get(25)==3: #CHECK IF HAVE 3, 25 dollars
                bal[25]-=3
                bal[i]+=1
            else:
                return "NO"
    return "YES"