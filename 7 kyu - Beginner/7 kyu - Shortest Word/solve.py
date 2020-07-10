def find_short(s):
    l =  [len(i) for i in s.split(" ")] 
    return min(l) # l: shortest word length