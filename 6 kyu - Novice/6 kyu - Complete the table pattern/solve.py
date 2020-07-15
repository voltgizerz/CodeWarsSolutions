def pattern(rows, columns, s):
    table =[]
    char = [x for x in s]
    index = 0
    for i in range(rows*2+1):
        line ="+"
        if i%2==0:
            line += columns * '---+'
            table.append(line) #INSERTING LINE 
        else:
            str = "|"
            cnt = 0
            if index != len(char):
                for x in range(index,len(char)):
                    str+= f" {char[x]} |"
                    cnt +=1
                    if cnt == columns: break 
                index = x+1
                if cnt<columns: str+= (columns-cnt) * '   |' #ADDING EMPYT 
                table.append(str) #INSERTING ROW CHAR 
            else:
                 str += columns * '   |' 
                 table.append(str) #INSERTING EMPTY ROW 
    return "\n".join(table)