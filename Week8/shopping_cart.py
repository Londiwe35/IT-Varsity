#Create shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter food item or press 'q' to quit: ")
    if food == 'q':
        break
    else:
        price = float(input(f"Enter price for the {food} : R"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR SHOPPING CART-------")

for food in foods:
    print(food, end= "")
    
for price in prices:
    total += price
    
print("\n")    
print(f"Total: R{total}")