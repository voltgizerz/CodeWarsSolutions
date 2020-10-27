from string import ascii_letters
def play_pass(s, n):
    word=""
    for x,s in enumerate(s):
        if s.isnumeric():
            word+= str(9-int(s))
        elif s.isalpha() and x%2==0:
            word+= ascii_letters[(ascii_letters.index(s) + n)%26].upper()
        elif s.isalpha() and x%2!=0:
            word+= ascii_letters[(ascii_letters.index(s) + n)%26].lower()
        else:
            word+=s
    return word[::-1]