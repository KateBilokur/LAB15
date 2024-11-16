import pandas as pd

# Створення словника з оцінками студентів
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Math': [85, 92, 78, 95, 88],
    'Physics': [75, 80, 82, 90, 85],
    'Chemistry': [90, 85, 78, 92, 88]
}

# Створення DataFrame
df = pd.DataFrame(data)
print(df)

# Обчислення середнього балу з математики для всіх студентів
avg_math = df['Math'].mean()
print("Середній бал з математики:", avg_math)

# Обчислення максимального балу з фізики
max_physics = df['Physics'].max()
print("Максимальний бал з фізики:", max_physics)

# Групування за предметами та обчислення середнього балу
grouped = df.groupby('Student')
avg_scores = grouped.mean()
print("Середні бали кожного студента:\n", avg_scores)

# Групування за предметами та обчислення сумарного балу
total_scores = grouped.sum()
print("Сумарні бали кожного студента:\n", total_scores)
