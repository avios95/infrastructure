import mysql.connector
from faker import Factory
from mysql.connector import Error
import re
import random

########################### START structure db ########################
# owner ==> id|address|city|first_name|last_name|telephone
# pets ==> id|birth_date|name|owner_id|type_id
# specialties ==> id|name
# types ==> id|name
# vet_spetialties ==> specialty_id|vet_id
# vets ==> id|first_name|last_name
# visits ==> id|description|pet_id|visit_date
########################### END structure db  #########################


############################# def ##################################
def run_write_query(SQLquery):
    try:
        host = '123.123.123.123'
        db = 'db'
        user = 'user'
        passwdord = 'passwdord'
        conn = mysql.connector.connect(host=host, database=db, user=user, password=passwdord)
        if conn.is_connected():
            print('Connected to MySQL database, run query: ' + SQLquery)
            cursor = conn.cursor()
            cursor.execute(SQLquery)
            conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()


def gen_data_to_owner():
    fake = Factory.create()
    address = fake.address()
    address = re.sub('\n.*', '', address)
    city = fake.city()
    first_name = fake.first_name()
    last_name = fake.last_name()
    telephone = fake.msisdn()
    query = "INSERT owners (address, city, first_name, last_name, telephone) VALUES ( '" + address + "','" + city + "','" + first_name + "','" + last_name + "','" + telephone + "');"
    run_write_query(query)


def gen_data_to_pets():
    fake = Factory.create()
    name = fake.first_name()
    birth_date = str(fake.date())
    owner_id = str(fake.random_int(min=1, max=11))
    type_id = str(fake.random_int(min=1, max=6))
    query = "INSERT pets (birth_date, name, owner_id, type_id) VALUES ( '" + birth_date + "','" + name + "','" + owner_id + "','" + type_id + "');"
    run_write_query(query)

def gen_data_to_vets():
    fake = Factory.create()
    first_name = fake.first_name()
    last_name = fake.last_name()
    query = "INSERT vets (first_name, last_name) VALUES ( '" + first_name + "','" + last_name + "');"
    run_write_query(query)


def gen_data_to_visits():
    fake = Factory.create()
    pet_id = str(fake.random_int(min=1, max=10))
    visit_date = str(fake.date())
    description = fake.bs()
    query = "INSERT visits (description, pet_id, visit_date) VALUES ( '" + description + "','" + pet_id + "','" + visit_date + "');"
    run_write_query(query)


# gen_data_to_owner()
# gen_data_to_pets()
# gen_data_to_vets()
# gen_data_to_visits()

functions = ['gen_data_to_owner', 'gen_data_to_pets', 'gen_data_to_vets', 'gen_data_to_visits']
r = random.choice(functions)
if r == "gen_data_to_owner": gen_data_to_owner()
if r == "gen_data_to_pets": gen_data_to_pets()
if r == "gen_data_to_vets": gen_data_to_vets()
if r == "gen_data_to_visits": gen_data_to_visits()
