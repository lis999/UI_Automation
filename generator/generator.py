import random

from data.data import Person, Color, Date
from faker import Faker

fake = Faker()
Faker.seed()


def generated_person():
    yield Person(
        full_name=fake.first_name() + " " + fake.last_name(),
        firstname=fake.first_name(),
        lastname=fake.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(60000, 110000),
        department=fake.job(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address(),
        mobile=fake.msisdn(),
    )


def generated_file():
    path = rf'C:\Users\Sergey\Projects\UI_Automation\files\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Something from somewhere{random.randint(0, 999)}')
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Violet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=fake.year(),
        month=fake.month_name(),
        day=fake.day_of_month(),
        time='12:00',
    )
