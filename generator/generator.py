from data.data import Person
from faker import Faker
import random

faker = Faker()
Faker.seed()


def generate_person():
    return Person(
        full_name=faker.first_name() + faker.last_name(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        age=random.randint(18, 65),
        salary=random.randint(1000, 10000),
        department=faker.job(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address()
    )


def generate_count_rows():
    counts = [5, 10, 20, 25, 50, 100]
    count = random.choice(counts)
    return count