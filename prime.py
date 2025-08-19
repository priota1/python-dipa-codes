
while True:
    num = input("enter a number :")
    if num.lower() == "exit":
        print("loop terminated")
        break
    num = int(num)
    if num<=1 :
     print(f"not a \nprime")  #printing not primr
    else:
     is_prime = True
     for n in range (2,num):

      if num%n==0 :
       print(f"not a  prime ")
       is_prime=False
       break
     if is_prime : print("prime")