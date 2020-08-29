def array(string):
    s = string.split(",")
    return None if len(s)<3 else " ".join(s[1:len(s)-1])