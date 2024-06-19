# WAP that checks if a string starts with a given prefix or ends witha given suffix
str=input("Enter a string: ")
a=input(str("Check_for_prefix_character:"))
b=input(str("Check_for_suffix_character:"))
if a==str[0]:
    print(str, "starts with", a)
else:
    print(str, "does not start with", a)
if b==str[-1]:
    print(str, "ends with", b)
else:
    print(str, "does not end with", b)
