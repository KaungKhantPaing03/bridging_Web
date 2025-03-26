buffet_foods = ("ham burger","pizza","fried chicken","ice cream","biryani")
print('Favorite Foods: ')
for food in buffet_foods:
    print(food)

#buffet_foods[0] = 'pasta'

buffet_foods = ("ham burger","pizza","fried chicken","ice cream","biryani","noodle","hotpot")
print("Revised Menu")
for ind, food in enumerate(buffet_foods): # index and value
    print(ind, food)
