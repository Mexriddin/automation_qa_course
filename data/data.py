from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None


@dataclass
class Student(Person):
    mobile: str = None
    date_of_birth: str = None
    gender: str = None
    subjects: list = None
    hobby: str = None


@dataclass
class Colors:
    colors_list: list = None
