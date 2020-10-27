def reverse_words(text):
    split = text.split(" ")
    for i in range(len(split)):
        split[i]= split[i][::-1]
            
    return " ".join(split)