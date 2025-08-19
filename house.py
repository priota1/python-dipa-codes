name=input("whats your name ?")
match name:
    case "harry" | "harmione" | "ron":
        print("griffendor")
    case "draco":
        print("sytherin")
    case _:
        print("who?")

