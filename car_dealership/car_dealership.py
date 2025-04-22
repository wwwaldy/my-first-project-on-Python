import time

audi_a_series = {
    'a4': {
        'brand': 'audi',
        'model': 'a4',
        'color': 'black',
        'year': '2016',
        'price': '19.500$',
        'engine': '2.0 TFSI',
        'mileage': '233.000 km',
    },
    'a5': {
        'brand': 'audi',
        'model': 'a5',
        'color': 'white',
        'year': '2018',
        'price': '31.000$',
        'engine': '2.0 TFSI',
        'mileage': '80.000 km',
    },
    'a7': {
        'brand': 'audi',
        'model': 'a7',
        'color': 'black',
        'year': '2023',
        'price': '63.000$',
        'engine': '3.0 TFSI',
        'mileage': '49.000 km',
    },
}

print('Добро пожаловать в автосалон!')

print(audi_a_series['a7']['price'])
