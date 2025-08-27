# nested loop 

rows= int(input("Enter the number of Rows "))
columns=int(input("Enter the number of Columns ")) 
sign= input("Enter your sign: ")

for x in range (rows):
    for y in range (columns):
        print(sign, end= "")
    print()