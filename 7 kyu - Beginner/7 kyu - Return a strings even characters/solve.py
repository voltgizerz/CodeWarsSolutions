def even_chars(st): 
    return "invalid string" if len(st)<2 or len(st)>100 else [char for  i, char in enumerate(str(st)) if i % 2 == 1]