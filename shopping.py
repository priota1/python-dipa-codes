
item =[]

while True :
 data={}
 data["name"] = input("Enter an item: ")
 data["price"]=int(input("enter the price : "))
 item.append(data)
 choice = input("Add another item? (yes/no): ").lower()
 if choice!="yes":
  break
  
print("\nShopping List:")
for data in item:
    print(f"{data['name']} - ${data['price']}")  

   
