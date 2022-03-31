def repalce_string(st,a,b):
    st = st.replace(a,b)
    return st
def replace_char(st,a,b):
    st = st.replace(a,b)
    return st

st = "string is data type of cython"
print("preveious string : ",st)
st = repalce_string(st,"cython","Python")
print("after word replace : ",st)
st = replace_char(st,"d","D")
print("after char repalce : ",st)