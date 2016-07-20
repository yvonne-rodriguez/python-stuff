import random

print('''
''')
print("MENU")

food = [ "Chicken", "Steak", "Shrimp", "Rice", "Tofu", "Beef", "Turkey", "Ribs", "Lobster", "Fish"]
cooking = [ "Steamed", "Grilled", "Roasted", "Seasoned", "Fried", "Baked", "Sauteed", "Barbecued", "Marinated", "Boiled"]
adj = ["Creamy", "Spicy", "Buttery", "Browned", "Cheesy", "Crunchy", "Delectable", "Drizzled", "Delicate","Golden"]

food_length = len(food)
random_food = random.randint(0,food_length-1)

cook_length = len(cooking)
random_cook = random.randint(0,cook_length-1)

adj_length = len(adj)
random_adj = random.randint(0,adj_length-1)


for i in range(10):
    random_adj = random.randint(0,adj_length-1)
    random_cook = random.randint(0,cook_length-1)
    random_food = random.randint(0,food_length-1)
    print(i+1,adj[random_adj]+" "+cooking[random_cook]+" "+food[random_food])
    




