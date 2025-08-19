n=int(input("Enter a number :"))
if n<=1 :
 print("not a prime number")
else:
 for i in range (2,n-1):
  if n%i==0 :
   print(f"Not a Prime Number")
   break
 else :
  print(f" Prime Number")
