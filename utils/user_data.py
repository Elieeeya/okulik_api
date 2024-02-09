import random

from faker import Faker


class Users:
    fake_en = Faker()
    fake_ru = Faker('ru_RU')

    title = fake_en.name()
    job = fake_en.job()
    id = random.randint(1, 100)

    title_ru = fake_ru.name()
    job_ru = fake_ru.job()
