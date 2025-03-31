usernames = ['admin','robert','sophia','marie']
print(len(usernames))
if len(usernames) == 0:
    print("We need to find some users.")
else:
    for user in range(0,len(usernames)):
        print(usernames.pop())
print("After popping out users!!")
print(usernames)