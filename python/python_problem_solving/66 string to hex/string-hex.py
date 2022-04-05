def string_hex(st):
    he = []
    for i in range(len(st)):
        s = hex(ord(st[i]))
        he.append(str(s))
    print("hex in string : ","".join(he))

st = input("Enter string : ")
string_hex(st)