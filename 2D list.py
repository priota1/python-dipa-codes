#2D list
fruits=    ["Apple","Banana","kiwi"]
vegetables=["Potato","Spinach","basil"]
meats=     ["chicken","Lamb","Goat"]

groceries =[fruits,vegetables,meats]

print(groceries[1][2])

items = [["pin","clip","thong"],["net","sponge","brush"],["pen","pencile","eraser"]]

for coolection in items:
    for things in coolection:
        print(things, end=" ")
    print()
