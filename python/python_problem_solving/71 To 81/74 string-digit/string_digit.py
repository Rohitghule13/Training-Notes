def array_string(st):
    arr = []
    num = "1234567890"
    for i in st:
        if any(c for c in i if c in num):
            arr.append(i)
    return arr
    

st = ["Rohit","kajska","asjakw","ajwh12"]
print(array_string(st))