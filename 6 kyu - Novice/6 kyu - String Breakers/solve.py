def string_breakers(n, st):
    st = st.replace(" ","")
    ans = [st[x:x+n] for x in range(0,len(st),n)]
    return "\n".join(ans)