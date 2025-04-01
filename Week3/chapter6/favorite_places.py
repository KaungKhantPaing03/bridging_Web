favorite_places = {
    'yati': ['POL','MDY','Sagaing'],
    'kevin' : ['YAY','Maungmakan','Ngapali'],
    'andrew' : ['Taunggyi','InnLay','Pintaya']
}

for name, places in favorite_places.items():
    print(f"Name: {name}")
    print("Favorite Places:")
    for place in places:
        print("\t",place)
    print()