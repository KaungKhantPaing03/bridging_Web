prompt = "Enter your age: "
while True:
    age = int(input(prompt))
    if age == 0:
        break
    elif age < 3:
        price = 0
    elif age >= 3 and age <= 12:
        price = 10
    elif age > 12:
        price = 15
    print(f"Your movie ticket charges ${price} for your age {age}")