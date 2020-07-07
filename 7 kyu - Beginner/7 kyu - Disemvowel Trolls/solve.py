def disemvowel(string):
    text=""
    list = [char for char in string]
    for ele in list:
        if ele not in ["a","i","u","e","o","A","I","U","E","O"]: 
            text += ele 
    return text