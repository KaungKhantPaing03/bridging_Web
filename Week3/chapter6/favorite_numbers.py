favorite_numbers = {
    'marie':[1,3,4,7,9],
    'theingi':[2,5,6],
    'shweyee':[3,11,23],
    'bob':[5,6,7]
}
for user in favorite_numbers.keys():
    print(f"{user}'s favorite numbers")
    for number in favorite_numbers[user]:
        print(number, end=" ")
    print()