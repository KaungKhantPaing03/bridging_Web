my_foods = ['pizza','falafel','carrot cake'] #source
my_friend_foods = my_foods[:] #start 0 through the last item
print("My food list:")
print(my_foods)
print("friend's food list:")
print(my_friend_foods)
my_foods[0] = 'cheese pizza'
print(my_foods)
print('Friends food list' ,my_friend_foods)
print("After appending element into lists")
my_foods.append('cannoli')
my_friend_foods.append('ice cream')
print(my_foods)
print('Friends food list' ,my_friend_foods)