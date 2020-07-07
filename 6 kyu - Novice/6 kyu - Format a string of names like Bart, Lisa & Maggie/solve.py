def namelist(names):
    list=[]
    for i in range(len(names)):
        if len(names) !=1:
            if i == len(names)-1 : 
                list.append(" & "+names[i].get("name")) 
            else:
                if i == len(names)-2 : 
                    list.append(names[i].get("name"))
                else:
                     list.append(names[i].get("name")+', ')
        else:
            list.append(names[i].get("name"))
    return "".join(list)    