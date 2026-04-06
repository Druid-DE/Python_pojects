from sqlalchemy import create_engine
import pandas as pd


def main():
    # Подключение
    engine = create_engine('postgresql+psycopg2://postgres:postgres123@localhost:5432/etl_db')

    # 1. Читаем данные из БД
    df = pd.read_sql('SELECT id, name, salary, department FROM employees_orm', engine)

    if df.empty:
        print("❌ Нет данных в таблице employees_orm")
        return

    # 2. Вводим бонусы
    print("🎁 Введите бонусы для сотрудников:")
    for idx, row in df.iterrows():
        while True:
            try:
                bonus = int(input(f"Бонус для {row['name']}: "))
                df.loc[idx, 'bonus'] = bonus
                break
            except ValueError:
                print("❌ Введите число!")

    # 3. Считаем премии
    df['award'] = df['department'].map({
        'it': 15000,
        'hr': 10000,
        'business': 20000
    }).fillna(0)

    # 4. Итоговая зарплата
    df['full_salary'] = df['salary'] + df['award'] + df['bonus']

    # 5. Выводим отчёт
    print("\n📊 Отчёт:")
    print(df[['name', 'salary', 'award', 'bonus', 'full_salary']].to_string(index=False))
    print(f"\n💰 Общий фонд: {df['full_salary'].sum():,} ₽")
    print(f"📈 Средняя зарплата: {df['full_salary'].mean():,.2f} ₽")

    # 6. Сохраняем в БД (ЗАМЕНЯЕМ старую таблицу!)
    df.to_sql('salary_report', engine, if_exists='replace', index=False)
    print("\n✅ Отчёт сохранён в таблицу 'salary_report'")

    # 7. Сохраняем в CSV (опционально)
    df.to_csv('salary_report.csv', index=False, encoding='utf-8-sig')
    print("✅ Отчёт сохранён в salary_report.csv")

if __name__ == "__main__":
    main()