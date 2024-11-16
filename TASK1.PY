import pandas as pd
import matplotlib.pyplot as plt

# Зчитування даних з CSV файлу
file_path = 'bike_data.csv'  
data = pd.read_csv(file_path)

# Перетворення стовпця 'Date' у формат datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Додавання стовпця 'Month' для аналізу по місяцях
data['Month'] = data['Date'].dt.month

# Підрахунок загальної кількості велосипедистів за кожний місяць
monthly_counts = data.groupby('Month')[['Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 'Brébeuf']].sum().sum(axis=1)

# Визначення місяця з найбільшою кількістю велосипедистів
most_popular_month = monthly_counts.idxmax()
most_popular_count = monthly_counts.max()

print(f"Найбільш популярний місяць: {most_popular_month} з {most_popular_count} велосипедистами.")

# Побудова графіку кількості велосипедистів по місяцях
plt.figure(figsize=(12, 6))
plt.plot(monthly_counts.index, monthly_counts.values, marker='o', linestyle='-', color='b')
plt.title('Кількість велосипедистів по місяцях у 2009 році', fontsize=16)
plt.xlabel('Місяць', fontsize=14)
plt.ylabel('Кількість велосипедистів', fontsize=14)
plt.grid(True)
plt.xticks(range(1, 13))
plt.show()
