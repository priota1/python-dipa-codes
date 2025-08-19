
data {
    ["name":"apple","price":""]
    []
}
print(f"Enter an item : ")
data["name"] = input("Enter an item: ")
data["price"]=int(input("enter the price : "))
next=(input("Add another item? (yes/no): "))
if next=="yes":
 
