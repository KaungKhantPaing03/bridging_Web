#clist = [45,56,44,233,67] list, list()
#ctuple = (78,44,333,44) tuple, tuple()
# creating a dictionary with key and value pair
# item represent the key and value
alien_0 = {'color': 'green','point':5}
print(alien_0['color'])
print(alien_0['point'])
print("type",type(alien_0))
print('len',len(alien_0))
print(alien_0)

#adding new item including key and value
alien_0['x_position'] = 0
alien_0['y_position'] = 25

#viewing the whole raw dictionary
print(alien_0)
alien_0['x_position'] = 10

#after setting value 10 to x_pos
print(alien_0)
