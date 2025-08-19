even_count = 0
odd_count = 0
while True:
    number=input("enter a number: ")
    if number.lower()=="exit":
     print("termineted")
     break 
    if number.isdigit():
      number = int(number)
    count=0
    if number%2==0:
        print("even")
        even_count+=1
    else :
        print("odd")
        odd_count+=1
    
    print(f"\nYou entered {even_count} even number(s) and {odd_count} odd number(s).")