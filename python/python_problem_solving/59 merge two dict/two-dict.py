dictionary1 = {"Rohit":86,"Ajay":77,"Syyad":89,"suhas":89}
dictionary2 = {"Snehal":91,"Prachi":83,"Arundhati":78,"Swapna":81}
dictionary3 = dictionary1.copy()
for key, value in dictionary2.items():
    dictionary3[key] = value
print(dictionary3)
