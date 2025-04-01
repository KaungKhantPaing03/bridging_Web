pet_0 = {'name':'bobby',
         'type':'dog',
         'owner_name':'U Kyaw Min'}
pet_1 = {'name':'bunny',
         'type':'rabbit',
         'owner_name':'Daw Pan Nu'}
pet_2 = {'name':'pussy',
         'type':'cat',
         'owner_name':'U Tun Tun'}

pets = [pet_0,pet_1,pet_2]
for pet in pets:
    for key,value in pet.items():
        print(f"\t{key}: {value}")
    print()