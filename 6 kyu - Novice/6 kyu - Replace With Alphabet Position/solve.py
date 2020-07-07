def alphabet_position(text):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    value = ""
    for i in range(len(text)):
        if text[i].isalpha() == True:
            if i!=0: value +=" "
            value += str(alphabet.find(text[i].lower())+1)
    return value 