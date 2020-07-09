import re
def solution(string,markers):
    if markers:
        string =string.split("\n")
        for i in range(len(string)):
            replacer = (("["+"".join(markers)+"]").replace("-","\-")).replace("^","\^")
            split =(re.sub(replacer, "***", string[i])).split("***")
            string[i]= split[0].strip()
        return "\n".join(string)
    else:
        return string