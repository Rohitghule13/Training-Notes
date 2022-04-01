def remove_item(dictionary,name):
    if name in dictionary:
        dictionary.pop(name)
        print("removed")
        print("New Dictionary : ",dictionary)
    else:
        print("Given Name is not exist in the dictionary")
        return

dictionary = {"Rohit":86,"Ajay":77,"Syyad":89,"suhas":89,"Snehal":91,"Prachi":83,"Arundhati":78,"Swapna":81}
name = input("Enter Name to removing : ")
print("Exist dictionary : ",dictionary)
remove_item(dictionary,name)