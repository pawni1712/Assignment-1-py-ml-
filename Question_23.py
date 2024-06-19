#WAP that converts temperature from Celsius to Fahrenheit and Celsius and vica versa depending on the input
i=int(input("Enter 1 for input in Celsius and 0 for Fahrenheit: "))
T=int(input("Enter temperature: "))
if i==1:
    print(T,"degree Celsius= ", (9*T/5)+32, "degree Fahrenheit")
else:
    print(T,"degree Fahrenheit= ", (T-32)*5/9, "degree Celsius")
