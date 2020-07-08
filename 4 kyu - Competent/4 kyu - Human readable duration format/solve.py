import datetime
def format_duration(seconds):
    a = datetime.timedelta(seconds=seconds)
    list =[a.days//365,a.days%365,a.seconds//3600,(a.seconds//60)%60,(a.seconds%60)]
    name =[" years"," days"," hour"," minute"," second"]
    ans =[]
    for i in range(0,5):
        if list[i]==1:
            if name[i][-1]=="s": name[i]=name[i].replace(name[i][-1],"")
        else:
            if name[i][-1]!="s": name[i]=name[i]+"s"
    if list.count(0)==5:
        return "now"
    else:
        for cnt in range(len(list)):
            if list[cnt]!=0:
                ans.append(str(list[cnt])+name[cnt])
    if len(ans)==1:
        return ans[0]
    else:
        return ", ".join(ans[0:len(ans)-1])+" and "+ans[len(ans)-1]