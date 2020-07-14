def to_alternating_case(string):
    return "".join(x.lower() if x.isupper() else  x.upper() for x in string)