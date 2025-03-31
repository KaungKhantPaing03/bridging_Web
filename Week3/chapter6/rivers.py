rivers = {'nile':'egypt',
'amazon':'brazil',
'ayeyarwady':'myanmar',
'thanlwin':'myanmar',
'mekoung':'thailand'}

for river,country in rivers.items():
    print(f"{river.title()} runs through {country.title()}.")
    

print("Rivers")
for river in rivers:
    print("\t",river.title())

print("\nCountries")
for country in rivers.values():
    print("\t",country.title())