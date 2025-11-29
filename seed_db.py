import boto3
from decimal import Decimal

# 1. Initialize DynamoDB Resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1') # Change to your region
table = dynamodb.Table('f1_emissions')

# 2. The Data (F1 Race -> Nearest International Airport)
# Coordinates are for the AIRPORT, not the track (for flight calcs)
races_data = [
    {
        'race_id': 'melbourne',
        'circuit_name': 'Albert Park Circuit',
        'airport_code': 'MEL', # Melbourne Airport
        'latitude': Decimal('-37.673'),
        'longitude': Decimal('144.843')
    },
    {
        'race_id': 'shanghai',
        'circuit_name': 'Shanghai International Circuit',
        'airport_code': 'PVG', # Shanghai Pudong Int'l
        'latitude': Decimal('31.144'),
        'longitude': Decimal('121.808')
    },
    {
        'race_id': 'suzuka',
        'circuit_name': 'Suzuka Circuit',
        'airport_code': 'NGO', # Chubu Centrair Int'l
        'latitude': Decimal('34.858'),
        'longitude': Decimal('136.805')
    },
    {
        'race_id': 'jeddah',
        'circuit_name': 'Jeddah Corniche Circuit',
        'airport_code': 'JED', # King Abdulaziz Int'l
        'latitude': Decimal('21.670'),
        'longitude': Decimal('39.152')
    },
    {
        'race_id': 'miami',
        'circuit_name': 'Miami Grand Prix Circuit',
        'airport_code': 'MIA', # Miami International Airport
        'latitude': Decimal('25.795'),
        'longitude': Decimal('-80.290')
    },
    {
        'race_id': 'montreal',
        'circuit_name': 'Circuit Gilles Villeneuve',
        'airport_code': 'YUL', # Montreal-Pierre Elliott Trudeau Int'l
        'latitude': Decimal('45.457'),
        'longitude': Decimal('-73.749')
    },
    {
        'race_id': 'monaco',
        'circuit_name': 'Circuit de Monaco',
        'airport_code': 'NCE', # Nice Côte d\'Azur Airport
        'latitude': Decimal('43.658'),
        'longitude': Decimal('7.215')
    },
    {
        'race_id': 'barcelona',
        'circuit_name': 'Circuit de Barcelona-Catalunya',
        'airport_code': 'BCN', # Barcelona-El Prat Airport
        'latitude': Decimal('41.297'),
        'longitude': Decimal('2.078')
    },
    {
        'race_id': 'spielberg',
        'circuit_name': 'Red Bull Ring',
        'airport_code': 'VIE', # Vienna International Airport
        'latitude': Decimal('48.118'),
        'longitude': Decimal('16.566')
    },
    {
        'race_id': 'silverstone',
        'circuit_name': 'Silverstone Circuit',
        'airport_code': 'LHR', # London Heathrow Airport
        'latitude': Decimal('51.470'),
        'longitude': Decimal('-0.454')
    },
    {
        'race_id': 'spa',
        'circuit_name': 'Circuit de Spa-Francorchamps',
        'airport_code': 'BRU', # Brussels Airport
        'latitude': Decimal('50.901'),
        'longitude': Decimal('4.484')
    },
    {
        'race_id': 'hungaroring',
        'circuit_name': 'Hungaroring',
        'airport_code': 'BUD', # Budapest Ferenc Liszt Int'l
        'latitude': Decimal('47.436'),
        'longitude': Decimal('19.255')
    },
    {
        'race_id': 'zandvoort',
        'circuit_name': 'Circuit Zandvoort',
        'airport_code': 'AMS', # Amsterdam Schiphol Airport
        'latitude': Decimal('52.310'),
        'longitude': Decimal('4.768')
    },
    {
        'race_id': 'monza',
        'circuit_name': 'Autodromo Nazionale Monza',
        'airport_code': 'MXP', # Milan Malpensa Airport
        'latitude': Decimal('45.630'),
        'longitude': Decimal('8.723')
    },
    {
        'race_id': 'madrid',
        'circuit_name': 'Circuito de Madrid',
        'airport_code': 'MAD', # Adolfo Suárez Madrid–Barajas Airport
        'latitude': Decimal('40.471'),
        'longitude': Decimal('-3.562')
    },
    {
        'race_id': 'baku',
        'circuit_name': 'Baku City Circuit',
        'airport_code': 'GYD', # Heydar Aliyev Int'l
        'latitude': Decimal('40.467'),
        'longitude': Decimal('50.046')
    },
    {
        'race_id': 'singapore',
        'circuit_name': 'Marina Bay Street Circuit',
        'airport_code': 'SIN', # Singapore Changi Airport
        'latitude': Decimal('1.364'),
        'longitude': Decimal('103.991')
    },
    {
        'race_id': 'austin',
        'circuit_name': 'Circuit of the Americas',
        'airport_code': 'AUS', # Austin-Bergstrom Int'l
        'latitude': Decimal('30.194'),
        'longitude': Decimal('-97.669')
    },
    {
        'race_id': 'mexico_city',
        'circuit_name': 'Autódromo Hermanos Rodríguez',
        'airport_code': 'MEX', # Mexico City Int'l
        'latitude': Decimal('19.436'),
        'longitude': Decimal('-99.072')
    },
    {
        'race_id': 'sao_paulo',
        'circuit_name': 'Interlagos Circuit',
        'airport_code': 'GRU', # São Paulo-Guarulhos Int'l
        'latitude': Decimal('-23.435'),
        'longitude': Decimal('-46.473')
    },
    {
        'race_id': 'las_vegas',
        'circuit_name': 'Las Vegas Strip Circuit',
        'airport_code': 'LAS', # Harry Reid Int'l
        'latitude': Decimal('36.084'),
        'longitude': Decimal('-115.153')
    },
    {
        'race_id': 'qatar',
        'circuit_name': 'Losail International Circuit',
        'airport_code': 'DOH', # Hamad International Airport
        'latitude': Decimal('25.285'),
        'longitude': Decimal('51.531')
    },
    {
        'race_id': 'abu_dhabi',
        'circuit_name': 'Yas Marina Circuit',
        'airport_code': 'AUH', # Abu Dhabi Int'l
        'latitude': Decimal('24.433'),
        'longitude': Decimal('54.651')
    }
]

# 3. Insert Data
print("Seeding F1Circuits table...")
for race in races_data:
    try:
        table.put_item(Item=race)
        print(f"Added: {race['race_id']}")
    except Exception as e:
        print(f"Error adding {race['race_id']}: {e}")

print("Database population complete!")