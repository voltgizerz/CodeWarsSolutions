def find_missing_letter(chars):
    for i in range(len(chars)):
        if chr(ord(chars[i]) + 1)!=chars[i+1]:
            return  chr(ord(chars[i]) + 1)