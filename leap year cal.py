import calendar
a= input("enter the year: ")
a = int(a)
a = calendar.isleap (a)
if a==1:
	print("yes am a leap year")
else:
	print("no am not a leap year")