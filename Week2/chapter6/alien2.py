alien_0 = {'x_position':0, 'y_position':25,'speed':'medium'}
x_increment =0 
#move the alien to the right based on speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"moving after alien_0 {alien_0['x_position']}")