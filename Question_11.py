#WAP to print the first n numbers of the fibonacci series
n=int(input("Enter the number of terms: "))
def Fibonacci(n):
    a,b=0,1
    for i in range(1,n+1):
        if i==1:
            print(0)
        elif i==2 or i==3:
            print(1)
        else:
            a,b=b,a+b
            print(a+b)
Fibonacci(n)
