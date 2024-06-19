#WAP to check whether a given number is Even or Odd
x=int(input("Enter a Whole Number "))
def ODD_or_EVEN(x):
	if (x>=0):
		if ((x%2)==0):
			print(x, " is an EVEN number")
		else:
			print(x, " is a ODD number")
	else:
		print("INVALID NUMBER")
ODD_or_EVEN(x)
