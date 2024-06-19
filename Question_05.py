#WAP to take a input string and write it to a text file.
x=str(input("Enter content: "))
with open("Jiban.txt", "r+") as File:
    File.write(x)
    z=File.read()
    print(z)
