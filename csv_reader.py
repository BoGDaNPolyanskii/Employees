import matplotlib.pyplot as pl
import pandas as pd

try:
    employees = pd.read_csv('employees.csv')

    # Обрахунок кількості чоловіків і жінок загалом
    gender_count = employees['Стать'].value_counts()
    print(f"Кількість чоловіків: {gender_count.get('Чоловік', 0)}")
    print(f"Кількість жінок: {gender_count.get('Жінка', 0)}")

    # Графік по гендерам
    gender_count.plot(kind='bar', title='Стать співробітників')
    pl.ylabel('Кількість')
    pl.show()

    # Аналіз віку
    employees['Дата народження'] = pd.to_datetime(employees['Дата народження'])
    today = pd.Timestamp.now()
    employees['Вік'] = employees['Дата народження'].apply(lambda x: today.year - x.year - ((today.month, today.day) < (x.month, x.day)))

    age_categories = {
        'younger_18': employees[employees['Вік'] < 18],
        '18-45': employees[(employees['Вік'] >= 18) & (employees['Вік'] <= 45)],
        '45-70': employees[(employees['Вік'] > 45) & (employees['Вік'] <= 70)],
        'older_70': employees[employees['Вік'] > 70]
    }

    # Виведення кількості співробітників в кожній категорії та гендерний поділ
    for category, data in age_categories.items():
        male_count = data[data['Стать'] == 'Чоловік'].shape[0]
        female_count = data[data['Стать'] == 'Жінка'].shape[0]

        print(f"{category}: {len(data)} співробітників")
        print(f"  Чоловіків: {male_count}")
        print(f"  Жінок: {female_count}")

        # Графік по статях у кожній віковій категорії
        data['Стать'].value_counts().plot(kind='bar', title=f'{category} за статтю')
        pl.ylabel('Кількість')
        pl.show()

except FileNotFoundError:
    print("Помилка: CSV файл не знайдено.")

except Exception as e:
    print(f"Помилка: {e}")