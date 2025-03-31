usernames = ['admin','robert','sophia','marie']
for username in usernames:
    if username == 'admin':
        print("Hello Admin, Would you like to see status report?")
    else:
        print(f"Hello {username.title()}, Thank you for logging in again.")