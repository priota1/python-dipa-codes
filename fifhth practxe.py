
age=int(input("what year did you born? "))
current_year=2025
if age == exit:
   print("Program exited.")
elif age >=current_year:
    print("Invalid input! Birth year cannot be in the future.")
else :

 future_time=int(input("Enter the year you want to calculate age for: "))
 if future_time < age:
    print(f"Invalid input! The future year must be after your birth year.")
 else :
    result = future_time - age  
    print(f"In {future_time}, you will be {result} years old.")  
 
income = int(input("Salery :"))
expenses = int(input("how much do you spend ? "))
after_expense= income - expenses
print(f"you have {after_expense}")