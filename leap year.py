while True:
    year = input("Enter a number (or type 'exit' to stop): ")  # Take input as a string
    
    if year == "exit":  # If user types "exit", stop the loop
        print("Loop exited.")
        break

      
    elif year.isdigit :
      year = int(year)
      
      if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year!")
      else:
            print(f"{year} is not a leap year!")
    else :
       print("invalid")
             
    
 
