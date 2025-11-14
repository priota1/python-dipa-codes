number=int(input("Enter a number: "))
if number > 20 or number <10:
    print(f"Number out of range.")
elif number % 2== 0:
    print(f"even")
else:
    print(f"odd")