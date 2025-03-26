age = int(input("Enter your age: "))
# if age<4:
#     print("Admission cost is $0.")
# elif age<18:
#     print("Admission cost is $25.")
# else:
#     print("Admission cost is $40.")
    
if age<4:
    price = 0
elif age<18:
    price = 25
elif age< 65:
    price = 40
else:
    price = 20
    print(f"Admission cost is ${price}.")