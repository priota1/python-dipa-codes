command = ""
started = False  # ✅ Use only one flag

while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started!")

    elif command == "stop":
        if not started:
            print("Car is already stopped!")  # ✅ Fix: Make sure car was started before stopping
        else:
            started = False  # ✅ Stop the car
            print("Car stopped!")

    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)

    elif command == "quit":
        break

    else:
        print("Sorry, I don't understand.")



    

  




  

    