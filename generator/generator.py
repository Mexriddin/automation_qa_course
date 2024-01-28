import datetime
import os
import pathlib

from data.data import *
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


def generate_student():
    return Student(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        gender=random.choice(["Male", "Female", "Other"]),
        date_of_birth=faker.date_of_birth().strftime("%d %b %Y"),
        subjects=[random.choice(["Math", "Arts", "Physics", "Chemistry", "English", "Biology"]) for _ in range(2)],
        hobby=random.choice(["Sports", "Reading", "Music"]),
        current_address=faker.address(),
        mobile="".join([str(random.randint(0, 9)) for _ in range(10)])
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


def generate_jpeg():
    picture = "../data/sampleFile.jpeg"
    return os.path.abspath(picture)


def generate_colors(count):
    all__colors = ["Red", "Green", "Blue", "Yellow", "Aqua", "White", "Purple", "Violet", "Magenta", "Indigo", "Black"]
    colors = [random.choice(all__colors) for _ in range(count)]
    print(colors)
    return Colors(colors_list=colors)