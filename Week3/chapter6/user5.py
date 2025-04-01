users = [
    {'username':'aeinstein',
            'first': 'albert',
            'last': 'einstein',
            'location': 'pinceton',
        },
    {'username':'mcurie',
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
    },
    {'username':'elonmusk',
            'first':'elon',
            'last':'musk',
            'location':'washinton D.C',
    },
    {'username':'dtrump',
        'first':'donald',
        'last':'trump',
        'location':'washinton D.C',
    },
    {'username':'jbiden',
        'first':'joe',
        'last':'biden',
        'location':'scranton'
    }
]
for user in users: #iterable
    for key,value in user.items():
        print(f"{key}: {value.title()}")
    print()