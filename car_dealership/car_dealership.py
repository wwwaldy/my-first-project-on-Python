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
audi_rs_series = {
    'rs4': {
        'brand': 'audi',
        'model': 'rs4',
        'color': 'blue',
        'year': '2020',
        'price': '70.000$',
        'engine': '2.9 TFSI',
        'mileage': '20.000 km',
    },
    'rs5': {
        'brand': 'audi',
        'model': 'rs5',
        'color': 'red',
        'year': '2021',
        'price': '80.000$',
        'engine': '2.9 TFSI',
        'mileage': '15.000 km',
        'rs7': {
            'brand': 'audi',
            'model': 'rs7',
            'color': 'black',
            'year': '2022',
            'price': '100.000$',
            'engine': '4.0 TFSI',
            'mileage': '10.000 km',
        },
    },
}

print('Добро пожаловать в автосалон!')

print(audi_a_series['a7']['price'])
