#WAP for a simple Calculator that takes 2 numbers and an operator and prints the result
a,b,c=int(input("Enter a number: ")), int(input("Enter another number: ")), input("Enter operator{+,-,*,/}: ")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("Invalid Input: ")
