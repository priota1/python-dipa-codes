num = int(input("Enter a number: "))

if num > 0 and num%2==0:
    print(f"The number is Positive even.")
elif num > 0 and num %2 !=0:
    print(f"The number is Positive odd")
elif num < 0:
    print(f"The number is negative.")
else:
    print(f"The number is zero.")