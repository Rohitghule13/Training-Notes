vowels = "aeiouAEIOU"
char = input("Enter character only one : ")
if char in vowels:
    print(f"'{char}' is vowel")
else:
    print(f"'{char}' is consonant")