start= '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour to survive. Don't touch the walls.”
There is a hallway to your right and to your left.
'''
left ='''You decide to go left and the coast is clear and you see your room
in the distance.
'''
right= '''You choose to go right and you run into a ferocious tiger,
you have a bag with supplies and you see a rock nearby
'''
fight = '''you run towards the tiger, but your bag has nothing to defend yourself with. 
Tiger eats you alive.
'''
rock = '''you throw the rock at the tiger and it gets lodged in his eye; 
you run away from him as he struggles with the rock in his eye.
'''
run = '''you try to run away but the tiger goes after you, he's faster than
you and catches up to you and eats you alive
'''
 


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print(left)

if user_input == "right":
    print(right) 
	
print("Type your choice:'rock','fight' or 'run away'")
choice=input()
if choice == "fight":
	print(fight)
	
if choice == "rock":
	print(rock)
	
if choice == "run":
	print(run)
	
		

  
