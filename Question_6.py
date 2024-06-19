#WAP to read a file and print its content
with open("Jiban.txt", "r") as File:
  z=File.readlines()
  for i in z:
    print(i)
