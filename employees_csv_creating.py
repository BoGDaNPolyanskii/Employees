import csv
import random
from faker import Faker

fake = Faker(locale='uk_UA')

# Створення словника для генерації по-батькові
middle_names = {
    'male': [
        'Андрійович', 'Богданович', 'Васильович', 'Володимирович', 'Григорович', 'Дмитрович',
        'Євгенович', 'Іванович', 'Ігорович', 'Леонідович', 'Михайлович', 'Олегович',
        'Олександрович', 'Олексійович', 'Петрович', 'Сергійович', 'Степанович', 'Юрійович'
    ],
    'female': [
        'Андріївна', 'Богданівна', 'Василівна', 'Володимирівна', 'Григорівна', 'Дмитрівна',
        'Євгенівна', 'Іванівна', 'Ігорівна', 'Леонідівна', 'Михайлівна', 'Олегівна',
        'Олександрівна', 'Олексіївна', 'Петрівна', 'Сергіївна', 'Степанівна', 'Юріївна'
    ]
}

# Отримання по батькові відповідно до статі
def get_middle_name(gender):
    return random.choice(middle_names[gender])

# Створення записів
def generate_employee_data(gender):
    if gender == 'male':
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        middle_name = get_middle_name('male')
        gender_str = 'Чоловік'
    else:
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
        middle_name = get_middle_name('female')
        gender_str = 'Жінка'

    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=86)
    job_title = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, middle_name, gender_str, birth_date, job_title, city, address, phone, email]

# Створення CSV файлу
def create_employee_csv(filename, num_employees=2000, male_percentage=0.6):
    num_males = int(num_employees * male_percentage)  # 60% чоловіків
    num_females = num_employees - num_males  # 40% жінок
    employees = []

    # Генерація даних для чоловіків
    for _ in range(num_males):
        employees.append(generate_employee_data('male'))

    # Генерація даних для жінок
    for _ in range(num_females):
        employees.append(generate_employee_data('female'))

    # Перемішування записів для довільного порядку
    random.shuffle(employees)

    # Запис даних в CSV файл
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання',
            'Адреса проживання', 'Телефон', 'Email'
        ])

        for employee in employees:
            writer.writerow(employee)

create_employee_csv('employees.csv')