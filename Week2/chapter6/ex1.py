person = {'first_name':'Brian','last_name':'Davidson','age':23,'city':'Mandalay'}

#printing raw form

print(person)
print(person.get('first_name')) #when using[], it raises an exception when key does not 
print(person.get('last_name'))
print(person.get('age'))
print(person.get('city'))