from faker import Factory
import re, requests, random

def_url = "http://123.123.123.123"


def run_POST(url, data):
    s = requests.Session()
    s.post(url, data=data, headers=dict(Referer=url))
    print(url)
    print(data)


def gen_data_to_owner():
    fake = Factory.create()
    address = fake.address()
    address = re.sub('\n.*', '', address)
    city = fake.city()
    first_name = fake.first_name()
    last_name = fake.last_name()
    telephone = fake.msisdn()

    url = def_url + '/owners/new'
    data = {
        'firstName': first_name,
        'lastName': last_name,
        'address': address,
        'city': city,
        'telephone': telephone
    }
    run_POST(url, data)


def gen_data_to_pets():
    type = ['cat', 'dog', 'lizard', 'snake', 'bird', 'hamster']

    fake = Factory.create()
    name = fake.first_name()
    birth_date = str(fake.date())
    owner_id = str(fake.random_int(min=1, max=11))
    type_id = random.choice(type)

    url = def_url + '/owners/' + owner_id + '/pets/new'
    data = {
        'name': name,
        'birthDate': birth_date,
        'type': type_id
    }
    run_POST(url, data)


def gen_data_to_visits():
    fake = Factory.create()
    pet_id = str(fake.random_int(min=1, max=10))
    visit_date = str(fake.date())
    description = fake.bs()

    url = def_url + '/owners/1/pets/' + pet_id + '/visits/new'
    data = {
        'date': visit_date,
        'description': description,
        'petId': pet_id
    }
    run_POST(url, data)


# gen_data_to_owner()
# gen_data_to_pets()
# gen_data_to_visits()

function = ['gen_data_to_owner', 'gen_data_to_pets', 'gen_data_to_visits']
r = random.choice(function)
if r == "gen_data_to_owner": gen_data_to_owner()
if r == "gen_data_to_pets": gen_data_to_pets()
if r == "gen_data_to_visits": gen_data_to_visits()
