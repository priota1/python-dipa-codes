# if and else 
import math

operator= input("Enter an operator (+ - * /): ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if operator == "+" :
 print(f"The result is {round(num1 + num2),3}")

elif operator == "-" :

 print(f"The result is {round(num1 - num2,3)}")

elif operator == "*":

 print(f"The result is {round(num1 * num2,3)}")

elif operator == "/":
 
 print(f"The result is {round(num1 / num2,3)}")

else:
 print("Try again.")