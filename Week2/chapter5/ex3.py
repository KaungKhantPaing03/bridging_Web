aliens_colors = ['green','red','yellow']


for color in aliens_colors:
    if color=='green':
        print("You earned 5 points.")
    else:
        print("You fail shooting.")
        
for color in aliens_colors:
    if color=='green':
        print("You earned 5 points.")
    elif color=='yellow':
        print("You earned 10 points.")
    else:
        print("You earned 15 points.")