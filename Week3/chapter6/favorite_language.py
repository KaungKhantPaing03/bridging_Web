favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite is {language.title()}")
    
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    
    if name in friends:
        language = favorite_languages[name].title()
        #language = favorite_languages.get(name).title()
        print(f"\t{name.title()}, I see you love {language}")
        

if 'erin' not in favorite_languages.keys():
    print("Erin, Please take our poll.")
    

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, Thank you for taking the poll.")
    

print("The following languages have been mentioned.")
for language in favorite_languages.values():
    print(language.title())

print("The following langauges have been mentioned.")
for language in set(favorite_languages.values()):
    print(language.title())
    
    

friends = ['kevin', 'sarah', 'phil', 'edward','robert','marie']
for friend in friends:
    if friend in favorite_languages.keys():
        print(f"{friend.title()}, Thant you for taking part the poll.")
    else:
        print(f"{friend.title()}, Please take the poll.")