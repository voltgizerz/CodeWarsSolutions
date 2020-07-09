import re
def solve(s):
    s = re.sub("[aeiou]", "-", s).split("-")
    value =[]
    for i in range(len(s)):
        sum =0
        for x in range (len(s[i])):
            sum+= ord(s[i][x])-96
        value.append(sum)
    return max(value)