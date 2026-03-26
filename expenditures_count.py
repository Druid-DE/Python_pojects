categories = {
    'required': 'обязательное',
    'products': 'продукты',
    'entertainment': 'развлечения'
}
def get_expenditures(category_name):
    try:
        expenditures = input(f'Введите расходы на {categories[category_name]}: ').split()
        return list(map(int, expenditures))
    except ValueError:
        print(f"❌ Ошибка: введите числа для категории '{categories[category_name]}'")
        return []

req = get_expenditures('required')
prod = get_expenditures('products')
ent = get_expenditures('entertainment')


all_exp= int(sum(req) + sum(prod) + sum(ent))
expenditures_limit = input('Введите лимит расходов:')
try:
    print("\n📊 Отчёт по расходам:")
    print("-" * 50)
    print(f'Обязательные расходы: {sum(req)} рублей.')
    print(f'Расходы на продукты: {sum(prod)} рублей.')
    print(f'Расходы на развлечения: {sum(ent)} рублей.')
    print("-" * 50)
    print(f'Общие расходы: {all_exp} рублей.')
    print(f'Лимит: {expenditures_limit} рублей.')
    if all_exp < int(expenditures_limit):
        print(f'Вы сэкономили {int(expenditures_limit) - all_exp} рублей!')
    else:
        print(f'Лимит расходов превышен на {all_exp - int(expenditures_limit)} рублей!')
except ValueError:
    print(f"❌ Ошибка: введите числовое значение для категории '{expenditures_limit}'")