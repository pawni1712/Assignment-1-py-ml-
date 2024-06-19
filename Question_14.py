#WAp that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
lines=[]
print("Enter any number of desired lines. To exit, enter an empty line")
while True:
		l=input()
		if l:
				lines.append(l)
		else:
				break;
print("The parrot response:\n")
for i in lines:
		print(i)
