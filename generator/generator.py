import datetime
import os
import pathlib

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


def random_count_rows():
    counts = [5, 10, 20, 25, 50, 100]
    count = random.choice(counts)
    return count


def random_click_type():
    click_types = ['double', 'right', 'click']
    click_type = random.choice(click_types)
    return click_type


def generate_file():
    path = f"../artifacts/upload_files/file_test_{random.randint(1, 10000)}.txt"
    with open(path, 'w+') as f:
        f.write(f"Hello, World {random.randint(1, 1000)}")
    return os.path.abspath(path)
