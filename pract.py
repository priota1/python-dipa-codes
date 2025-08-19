
a=int(input("Choose conversion:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter your choice: "))
if a==1:
    c=float(input("enter tempareture "))
    fahrenheit = (c * 1.8) + 32
    print (f"{fahrenheit:.2f}")
elif a==2:
    f=float(input("enter tempareture "))
    celcius = (f - 32) / 1.8
    print(f" {celcius:.2f}")
else :
    print("invalid")
