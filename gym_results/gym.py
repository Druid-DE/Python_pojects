import pandas as pd


def load_standards(filepath):
    """Загружает таблицу стандартов"""
    df = pd.read_csv(filepath)
    return df


def calculate_epley_max(weight, reps):
    """Считает разовый максимум по формуле Эпли"""
    if reps == 0:
        return weight
    return round(weight * (1 + reps / 30), 1)


def evaluate_result(total, standards_df):
    """Сравнивает результат с таблицей и возвращает оценку"""
    # Находим максимальный уровень, который спортсмен достиг
    for idx, row in standards_df.iterrows():
        if total <= row['bench'] + row['deadlift'] + row['squats']:
            return f"Уровень: {idx + 1} (из {len(standards_df)})"
    return f"Уровень: {len(standards_df)}+ (Элита!)"


def get_feedback(total, standards_df):
    """Даёт текстовую оценку результата"""
    max_total = standards_df[['bench', 'deadlift', 'squats']].sum(axis=1).max()
    percentage = (total / max_total) * 100

    if percentage >= 100:
        return "🏆 Элитный уровень! Ты машина!"
    elif percentage >= 90:
        return "🔥 Отличный результат! Почти элита!"
    elif percentage >= 75:
        return "💪 Хороший уровень! Продолжай расти!"
    elif percentage >= 60:
        return "👍 Неплохо! Есть куда расти!"
    else:
        return "📈 Продолжай тренироваться! Всё получится!"


def main():
    # Загружаем таблицу стандартов
    standards = load_standards('gym_score.csv')

    print("🏋️ Введи свои результаты:\n")

    # Ввод данных
    bench = int(input('Жим лёжа (кг): '))
    bench_reps = int(input('Количество повторений: '))

    deadlift = int(input('\nСтановая тяга (кг): '))
    deadlift_reps = int(input('Количество повторений: '))

    squats = int(input('\nПриседания (кг): '))
    squats_reps = int(input('Количество повторений: '))

    # Расчёт разового максимума
    bench_max = calculate_epley_max(bench, bench_reps)
    deadlift_max = calculate_epley_max(deadlift, deadlift_reps)
    squats_max = calculate_epley_max(squats, squats_reps)

    total = round(bench_max + deadlift_max + squats_max, 1)

    # Вывод результатов
    print("\n" + "=" * 60)
    print("📊 ТВОИ РЕЗУЛЬТАТЫ:")
    print("=" * 60)
    print(f"💪 Жим лёжа:    {bench_max:>6} кг (на 1 раз)")
    print(f"🏋️ Становая:    {deadlift_max:>6} кг (на 1 раз)")
    print(f"🦵 Приседания:  {squats_max:>6} кг (на 1 раз)")
    print("=" * 60)
    print(f"🎯 СУММА В ТРОЕБОРЬЕ: {total} кг!")
    print("=" * 60)

    # Сравнение с таблицей
    print("\n📈 СРАВНЕНИЕ СО СТАНДАРТАМИ:")
    print(evaluate_result(total, standards))
    print(get_feedback(total, standards))

    # Детальная информация по каждому упражнению
    print("\n📊 ДЕТАЛИЗАЦИЯ:")
    for idx, row in standards.iterrows():
        std_total = row['bench'] + row['deadlift'] + row['squats']
        if total >= std_total:
            print(f"✅ Уровень {idx + 1}: {std_total} кг — ДОСТИГНУТ")
        else:
            diff = round(std_total - total, 1)
            print(f"⏳ Уровень {idx + 1}: {std_total} кг — не хватает {diff} кг")
            break


if __name__ == "__main__":
    main()