# shopping cart 
foods= []
prices=[]
total = 0  

while True:
    food = input(" Enter a food to buy(q to quit): ")
    if food.lower()== "q":
        break
    else:
        price=float(input("Enter the prices of {food} : "))
        foods.append(food)
        prices.append(price)
print("----your cart is----")
for food in foods:
  
  print(food,end=" ")  

for price in prices:
   total+=price 

print()
print(f"Your total is: {total:.2f}")  

foods = ["apple", "bread", "milk"]
prices = [2.5, 1.75, 3.0]

for food, price in zip(foods, prices):
    print(f"{food} - ${price}")
