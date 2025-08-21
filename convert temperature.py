# convert temperature 

temp = float(input(" Enter the temperature: "))
unit = input("Is this temperature Fahrenheit or Celsius (C/F): ")

if unit == "F":
    temp = round((temp - 32)*5/9 ,1)
    print(f"The temperature in Celsius is: {temp}")

elif unit == "C":
    temp = round((9*temp)/5+32)
    print(f"The temperature in fahrenheit is: {temp}")
else:
    print("Not valid")
