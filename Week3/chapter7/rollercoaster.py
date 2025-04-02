height = input("How tall are you, in inches? ") #accepts user input as a string
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")