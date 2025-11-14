age=int(input("Enter your age: "))
income=int(input("Enter your income: "))
if age >= 18 and income >= 30000: 
    print("Eligable")
elif age >= 18 and income < 30000:
     print ("Not eligible due to low income")
else:
    print ("Not eligible due to age")