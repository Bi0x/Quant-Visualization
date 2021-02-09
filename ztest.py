from pyecharts.faker import Faker
print([list(z) for z in zip(Faker.choose(), Faker.values())])