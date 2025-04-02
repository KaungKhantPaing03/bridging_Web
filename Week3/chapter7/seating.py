no_users = input("How many people will you join the dinner?: ")
no_users = int(no_users)
if no_users > 8:
    print("You need to wait for a minute.")
else:
    print("The table is ready.")