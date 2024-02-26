def validBraces(str):
    stacks = []
    braces = {"}": "{","]":"[",")":"("}
    for i in str:
        if len(stacks) != 0 and braces.get(i) == stacks[-1]:
            stacks.pop()
            continue

        stacks.append(i)

    return len(stacks) == 0