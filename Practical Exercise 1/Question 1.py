#Ask the user to enter the day(s)
days = int(input("Enter the Number of Days"))

#Shows how many seconds,hours,minutes are in one day
seconds = 60
minutes = 60
hours = 24

#Calculating the number of seconds in the day(s) entered
print("Seconds in %d day/s are %d:" %(days,  days * hours * minutes*seconds))
