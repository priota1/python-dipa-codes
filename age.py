name = input("Enter your name: ")  # Take user's name
current_year=2025 # Take user's age

while True:
    birth_year=(input("Enter your birth year: "))

    if birth_year.lower()=="exit":
        print("terminited")
        break
    
    if birth_year.isdigit():  # Check if input is a number
        birth_year = int(birth_year)
    else:
        print("Invalid input! Please enter a valid number.")
        continue  # Ask for input again
    if birth_year>=current_year:
        print("Invalid birth year")
        continue
    
    age=current_year - birth_year
    if age<18:
            print("You are a minor")
    else :
            print("You are an adult")

    print(f"Hi {name}, you are {age} years old!") 
    break

