cities = {'yangon':{
    'country':'myanmar',
    'population':'5.1',
    'fact':'Yangon, formerly romanized as Rangoon, is the capital of the Yangon Region and the largest city of Myanmar.'
    },
          'Bangkok':{
              'country':'thailand',
              'population':'11.23',
              'fact':'Bangkok, officially known in Thai as Krung Thep Maha Nakhon and colloquially as Krung Thep, is the capital and most populous city of Thailand.'},
          'tokyo':{
              'country':'japan',
              'population':'37.1',
              'fact':'Tokyo, officially the Tokyo Metropolis, is the capital and most populous city in Japan.'},
          'auckland':{
              'country':'new zealand',
          'population':'1.7',
          'fact':'Auckland is a large metropolitan city in the North Island of New Zealand. It has an urban population of about 1,531,400 (June 2024).'},
          'toronto':{
              
              'country':'canada',
              'population':'2.8',
              'fact':'Toronto is the most populous city in Canada and the capital city of the Canadian province of Ontario.'
          }}

for city,info in cities.items():
    print(f"{city.title()}'s Information")
    for k,v in info.items():
        print(f"\t{k.title()} : {v.title()}")
    print()