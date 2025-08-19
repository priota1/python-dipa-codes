while True:
    num = input("enter a number :")
    if num.lower() == "exit":
        print("loop terminated")
        break

    num = int(num)
    if num % 2 == 0:
        print(" even")

    else:
        print("odd")
