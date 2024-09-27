from openpyxl import Workbook
import pandas as pd
from datetime import datetime

try:
    employees = pd.read_csv('employees.csv')

    # Обрахунок років
    employees['Дата народження'] = pd.to_datetime(employees['Дата народження'])
    today = pd.Timestamp(datetime.today())
    employees['Вік'] = employees['Дата народження'].apply(lambda x: today.year - x.year - ((today.month, today.day) < (x.month, x.day)))

    # Створення категорій років
    categories = {
        'younger_18': employees[employees['Вік'] < 18],
        '18-45': employees[(employees['Вік'] >= 18) & (employees['Вік'] <= 45)],
        '45-70': employees[(employees['Вік'] > 45) & (employees['Вік'] <= 70)],
        'older_70': employees[employees['Вік'] > 70]
    }

    # Запис даних в ексель
    try:
        with pd.ExcelWriter('employees.xlsx', engine='openpyxl') as writer:
            employees.to_excel(writer, sheet_name='all', index=False)
            for category, data in categories.items():
                data.to_excel(writer, sheet_name=category, index=False)
        print("Ok")

    except PermissionError:
        print("Помилка: файл не може бути створений, можливо він відкритий або у вас недостатньо прав.")

    except OSError as excel_error:
        print(f"Помилка: неможливо створити ексель файл через системну помилку. {excel_error}")

except FileNotFoundError:
    print("Помилка: CSV файл не знайдено.")

except Exception as e:
    print(f"Помилка: {e}")