while True:
  name = input("Enter your name : ")
  if name:
        break
  print("Name can't be empty. Try again.")
age = input("Enter your age: ")
while not age.isdigit():
    print("Please enter numbers only for age.")
    age = input("Enter your age: ")

age =int(age) 

print(f"Hello {name}, you will be {age+1} next year!")
print(f"In 5 years, you will be {age+5} years old.")