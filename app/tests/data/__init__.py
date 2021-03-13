from faker import Faker

fake = Faker()

def fake_unit(id):
    created_at = fake.date_time_between(start_date="-1y", end_date="now")
    name = fake.word()

    unit = {
        "id_int": id,
        "name": name,
        "code": f"{name}_code_{fake.word()}",
        "phone": fake.phone_number(),
        "description": fake.name(),
        "email": fake.email(),
        "dflag": False,
        "active": True,
        "created_at": created_at,
    }
    return unit

def units_list():
    units = []
    for i in range(1, 3):
        unit = fake_unit(id=i)
        units.append(unit)
    return units