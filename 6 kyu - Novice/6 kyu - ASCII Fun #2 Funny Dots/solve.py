def dot(n,m):
    funny =[]
    for i in range(m*2+1):
        if i%2==0:
            line ="+"
            line += n * '---+'
            funny.append(line) #INSERTING LINE 
        else:
            dots = "|"
            dots += n * ' o |'
            funny.append(dots) #INSERTING DOTS 
    return "\n".join(funny)