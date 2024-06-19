#WAP to read text from one text file and copy it to another text file
with open("Siesta.txt", "r") as x:
    t=x.readlines()
print("Text in Siesta: ", t)
with open("Vamos.txt", "a+") as File:
    print("Text in Vamos: ", File.readlines())
    File.writelines(t)
    File.seek(0)
    print("Text in Vamos after updation: ", File.readlines())
