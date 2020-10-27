def reverse_sentence(sentence):
    sentence = sentence.split(" ")
    for i in range(len(sentence)):
        sentence[i] = sentence[i][::-1]
    return " ".join(sentence)
        