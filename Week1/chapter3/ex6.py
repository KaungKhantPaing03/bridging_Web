









friends = ['Robert', 'Carl', 'Petra']
print("Wow! we've got a  bigger dinner table.")
friends.insert(0, 'Ko Ko')
friends.insert(2, 'Sandi')
friends.append('Yuya')
print(f"{friends[0]}, Please join the dinner tonight.")
print(f"{friends[1]}, Please join the dinner tonight.")
print(f"{friends[2]}, Please join the dinner tonight.")
print(f"{friends[3]}, Please join the dinner tonight.")
print(f"{friends[4]}, Please join the dinner tonight.")
print(f"{friends[5]}, Please join the dinner tonight.")

print("Unluckily, there is only two people we can invite for dinner.")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner. ")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner. ")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner. ")
print(f"{friends.pop()}, We are sorry. We can't invite you to dinner. ")

print(f"{friends[0]}, You are still invited to dinner ")
print(f"{friends[1]}, You are still invited to dinner. ")

del friends[0]
del friends[0]
print(f"After deleting two guests from list {friends}")
