student = {

}
while True:
    key = input("Enter a key (or type 'exit' to stop): ")
    
    if key.lower() == "exit":  # Stop when user types 'exit'
        break
    
    value = input(f"Enter value for {key}: ")
    student[key] = value  # Add to dictionary

# Print dictionary in the required format
print("\nHere is your dictionary:")
for key, value in student.items():
    
    print(f"{key}: {value}")


student["name"]="dipa"  # Output: Alice
print(student.get("city","not found"))  

student.popitem()
print(student.items())


