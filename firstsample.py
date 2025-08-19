colour=input(" What is your favorite colour? :")
print("My favorite colour is "+ colour)
age=int(input("What year did you born? :"))
current_year=2025
current_age=int(current_year - age)
print(f"you are {current_age} years old")
import datetime
year=int(input("Enter your birth year :"))
year2=int(input("enter a future year :"))
current=datetime.datetime.now().year
x=current-year
if year2 == current :
    print(f"You are currently {x} years old.")

elif year2>year :
 fort=year2-year
 print(f"In {year2} you will be {fort} years old")
else :
    print("Invalid input! Future year must be greater than birth year.")
