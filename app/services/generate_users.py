from faker import Faker


def generate(num_users=100):
    users = []

    for _ in range(num_users):
        name = Faker().first_name()
        email_users = Faker().email()
        user_data = f"{name} {email_users}"
        users.append(user_data)
    return users
