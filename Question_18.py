#WAP to check if two strings are anagram of each other
str=input("Enter a string: ")
str1=input("Enter another string: ")
l=list(str)
if (sorted(list(str))==sorted(list(str1))):
    print(str, "is an anagram of", str1)
else:
    print(str, "is not an anagram of", str1)
