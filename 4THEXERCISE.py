while True:
    n = input("Enter a number (or type 'exit' to stop): ")

    if n == "exit":  # Stop the loop if user types "exit"
        print("Loop exited.")
        break

    if n.isdigit():  # Check if input is a valid number
        n = int(n)

        for i in range(n, 0, -2):  # Count down by 2
            print(i)
    else:
        print("Invalid input. Please enter a number.")


        