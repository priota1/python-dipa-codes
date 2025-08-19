num=[3,4,5,6,7]
total=sum(num)
print(f"Total sum is : {total}")

fruit=("mango","apple","orange")
print(fruit)
student={"name" : "", "phone number":"" }
student["name"]=input("Enter your name : ")
student["phone number"]=int(input("Enter your phone number : "))
print("contact saved")
retrieve_name = input("Enter name to retrieve: ")
if retrieve_name ==student["name"]:

 print(f"{student['name']} number: {student['phone number']}")
else :
  print("Contact not found.")



