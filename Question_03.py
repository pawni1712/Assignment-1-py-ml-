#WAP that calculates the factorial of a given number
x=int(input("Enter a Whole Number "))
def fact(x):
    if (x==0 or x==1):
        return 1
    else:
        return (x*fact(x-1))
print("Factorial of", x, "is", fact(x))
