def spin_words(sentence):
    list= sentence.split(" ")
    text =""
    for i in range(len(list)):
        if i != 0:
             text +=" "
        if len(list[i]) >4:
            text +=list[i][::-1]
        else:
            text +=list[i]
    return text