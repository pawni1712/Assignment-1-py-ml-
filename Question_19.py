#WAP that removes all punctuation from a string
str=input("Enter a string with punctuation marks: \n")
p="!@#$%^&*()_{}|:<>?-=[]\;',./'"
for i in str:
    if i in p:
        str=str.replace(i,"")
print(str)
