def find_it(seq):
    found = 0
    for i in range(len(seq)):
        for z in range(len(seq)):
            found = seq.count(seq[z])
            if found%2==1:
                found = seq[z]
                break
    return found
