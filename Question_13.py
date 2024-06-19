#WAP that asks a user their birth Year and calculates their age
Birth_Year=input("Enter Birth year ")
Current_Year=input("Enter Current year ")
Y=int(input("Enter 1 if you have already celebrated your birthday this year "))
if 	Y==1:
		print("You are", int(Current_Year)-int(Birth_Year), "Year old.")
else:
		print("You are", int(Current_Year)-int(Birth_Year)-1, "Year old.")
