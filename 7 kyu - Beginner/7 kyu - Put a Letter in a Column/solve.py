def build_row_text(index, character):
    ans = ""
    for i in range(9):
        if i!=index:
            ans+="| "
        else:
            ans+=f"|{character}"
    return ans+"|"