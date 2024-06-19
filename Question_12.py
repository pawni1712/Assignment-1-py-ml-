#WAP that calculates the sum of digits of a given number
x=input("Enter a number: ")
sum=0
for i in x:
    sum+=int(i)
print("Sum of digits of", x, "is:", sum)
