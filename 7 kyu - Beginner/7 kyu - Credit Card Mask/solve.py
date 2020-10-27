# return masked string
def maskify(cc):
    return cc if cc=="" or len(cc)<5 else (len(cc)-4 )*"#"+cc[-4:]