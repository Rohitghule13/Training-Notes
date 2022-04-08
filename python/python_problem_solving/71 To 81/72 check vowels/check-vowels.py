vowels = "aeiouAEIOU" # used for reference for checking vowels 

char = input("Enter character only one : ") # getting input from console

if char in vowels: # if input character is vowel so if is follwed
    print(f"'{char}' is vowel") 

else:   # else is follwed when char is not present in vowel
    print(f"'{char}' is consonant")
    vowels.c