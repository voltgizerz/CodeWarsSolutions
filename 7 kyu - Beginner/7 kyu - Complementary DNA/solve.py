def DNA_strand(dna):
    dna = [ x for x in dna]
    for i in range(len(dna)):
        if dna[i]=='A':
            dna[i] = dna[i].replace("A","T")
        elif dna[i]=='T':
            dna[i] = dna[i].replace("T","A")
        elif dna[i]=='G':
            dna[i] = dna[i].replace("G","C")
        elif dna[i]=='C':
            dna[i] = dna[i].replace("C","G")
    return "".join(dna)