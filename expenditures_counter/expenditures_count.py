categories = {
    'required': 'обязательное',
    'products': 'продукты',
    'entertainment': 'развлечения'
}

def get_expenditures(category_key):
    """Запрашивает расходы по категории и возвращает список чисел"""
    try:
        data = input(f'Введите расходы на {categories[category_key]}: ').split(',')
        return list(map(int, data))
    except ValueError:
        print(f"❌ Ошибка: введите числа для категории '{categories[category_key]}'")
        return []


def main():
    # Собираем данные
    expenses = {key: get_expenditures(key) for key in categories}

    # Получаем лимит
    try:
        limit = int(input('Введите лимит расходов: '))
    except ValueError:
        print("❌ Ошибка: лимит должен быть числом!")
        return

    # Считаем итоги
    total = sum(sum(vals) for vals in expenses.values())

    # Выводим отчёт
    print("\n📊 Отчёт по расходам:")
    print("-" * 50)
    for key, name in categories.items():
        print(f'{name.capitalize()}: {sum(expenses[key])} рублей.')
    print("-" * 50)
    print(f'Общие расходы: {total} рублей.')
    print(f'Лимит: {limit} рублей.')

    if total <= limit:
        print(f'✅ Вы уложились в бюджет! Остаток: {limit - total} рублей.')
    else:
        print(f'❌ Превышение бюджета на {total - limit} рублей!')


if __name__ == "__main__":
    main()