# python compound interest calculator 

principle = 0
rate = 0
time = 0

while True :
    principle = float(input("Enter Your Principle "))
    if principle <0:
        print(f"Principle Cant be less than Zero ")
    else :
        break
    
while True :
     rate = float(input("Enter Interest Rate "))
     if rate < 0:
      print(f"Interest Rate cant be zero or less")

     else :
        break 

while True :
     time = int(input("Enter Year "))
     if time <0:
      print(f"Time cant be zero or less")

     else :
       break 

total = principle *pow((1+rate / 100 ),time)
print(f"Your total after {time} is ${total: .2f}")



