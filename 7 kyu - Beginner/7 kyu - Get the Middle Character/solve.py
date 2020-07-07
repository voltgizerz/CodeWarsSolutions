def get_middle(s):
    return s[int(len(s)/2)-1:int(len(s)/2)+1] if int(len(s))%2 == 0 else s[abs(int(len(s)/2))]
