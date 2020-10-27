def initials(name):
    name = name.split(" ")
    for i in range(len(name)):
        if i==len(name)-1:
            name[i] = name[i].title()
        else:
            name[i] = name[i][0].upper()
    return ".".join(name)