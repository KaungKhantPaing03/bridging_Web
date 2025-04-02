prompt = "Choose your topping that you would like to add to your pizza: "

while True:
    message = input(prompt)
    if message == 'quit':
        print("Thank you for buying our pizza.")
        break
    else: 
        print(f"We are adding your {message} topping to pizza.")