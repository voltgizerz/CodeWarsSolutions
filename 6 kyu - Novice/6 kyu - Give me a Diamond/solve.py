def diamond(n):
     list=[]
     for i in range(1,n+1,2):
        list.append(((i * '*').center(n)).rstrip())
     list.extend(sorted(list[0:len(list)-1],reverse=True))
     return None if (n%2==0 or n<0) else "\n".join(list)+"\n"