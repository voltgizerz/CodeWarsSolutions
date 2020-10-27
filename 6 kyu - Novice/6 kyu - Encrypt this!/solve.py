def encrypt_this(text):
    list = text.split(" ")
    for i in range(len(list)):
        if list[i]!="":
            if len(list[i])==1:
                list[i] = str(ord(list[i][0]))
            elif len(list[i])==2:
                list[i] = str(ord(list[i][0]))+list[i][1]
            elif len(list[i])==3:
                list[i] = str(ord(list[i][0]))+list[i][2]+list[i][1]  
            else:
                list[i] = str(ord(list[i][0]))+list[i][len(list[i])-1]+list[i][2:len(list[i])-1]+list[i][1]        
    return " ".join(list)