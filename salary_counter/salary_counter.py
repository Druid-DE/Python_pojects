def check_salary(department):
    if department == 'it':
        return 15000
    elif department == 'hr':
        return 10000
    elif department == 'business':
        return 20000
    else:
        return 0

employees = [
    {'name': 'Иван', 'salary': 25000, 'department': 'it'},
    {'name': 'Алексей', 'salary': 20000, 'department': 'hr'},
    {'name': 'Михаил', 'salary': 25000, 'department': 'it'},
    {'name': 'Ольга', 'salary': 30000, 'department': 'business'},
    {'name': 'Алёна', 'salary': 20000, 'department': 'hr'},
]

bonus = 0
for employee in employees:
    while True:
        try:
            bonus = int(input(f'Введите бонус {employee["name"]}: '))
            break
        except ValueError:
            print("❌ Бонус должен быть числом!")
    award = check_salary(employee["department"])
    employee['full_salary'] = employee["salary"] + award + bonus

print("\n📊 Отчёт по зарплате:")
print("-" * 50)
for employee in employees:
    print(f'{employee["name"]}: {employee["full_salary"]} ₽')
print("-" * 50)
total_payroll = sum(employee['full_salary'] for employee in employees)
avg_salary = total_payroll / len(employees)
print(f'Общий фонд зарплаты: {total_payroll} ₽')
print("-" * 50)
print(f'Средняя зарплата: {avg_salary} ₽')