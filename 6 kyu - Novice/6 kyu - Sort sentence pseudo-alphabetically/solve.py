import re
def pseudo_sort(st):
    st = re.sub("[?,!:'.;]", "", st)
    if st.strip()!="":
        st = st.split(" ")
        lower = sorted([x for x in st if x[0].islower()])
        upper = sorted([x for x in st if x[0].isupper()],reverse=True)
        return (" ".join(lower)+" "+" ".join(upper)).strip()
    return ""