def remove_parentheses(st):
    stacks = []

    newWord = ""
    for i in st:
        if len(stacks) == 0 and (i != "(" and i != ")"):
            newWord += i

        if i == ")" and stacks[-1] == "(":
            stacks.pop()
            continue
        else:
            if i == "(" or i == ")":
                stacks.append(i)

    return newWord
