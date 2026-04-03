import pandas as pd


def main():
    # Загружаем из CSV
    df = pd.read_csv('test_data.csv')

    # Вводим бонусы
    for idx, row in df.iterrows():
        while True:
            try:
                bonus = int(input(f"Бонус для {row['name']}: "))
                df.loc[idx, 'bonus'] = bonus
                break
            except ValueError:
                print("❌ Введите число!")

    # Считаем премии
    df['award'] = df['department'].map({
        'it': 15000,
        'hr': 10000,
        'business': 20000
    }).fillna(0)

    # Итоговая зарплата
    df['full_salary'] = df['salary'] + df['award'] + df['bonus']

    # Отчёт
    print("\n📊 Отчёт:")
    print(df[['name', 'full_salary']].to_string(index=False))
    print(f"\nОбщий фонд: {df['full_salary'].sum():,} ₽")

    # Сохраняем
    df.to_csv('salary_report.csv', index=False)
    print("✅ Сохранено в salary_report.csv")


if __name__ == "__main__":
    main()