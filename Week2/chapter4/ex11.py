my_foods = ['pizza','falafel','carrot cake'] 
my_foods.append('cheese pizza')
friends_foods = my_foods[:]
friends_foods.append('pineapple pizza')
print("My favorite pizzas are: ")
for pizza in my_foods:
    print(pizza)
print("My friend's favorite pizzas are: ")
for pizza in friends_foods:
    print(pizza)
