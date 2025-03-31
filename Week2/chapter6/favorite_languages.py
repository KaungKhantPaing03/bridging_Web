favourite_languages = {'jen': 'python', 'sarah': 'c', 'edward':'rust','phil':'python'}

language = favourite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

#accessing value with [] and get()
language2 = favourite_languages.get('je','person does not exist.')
print(language2.title())