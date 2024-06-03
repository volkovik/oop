import pandas as pd

dataset = pd.read_csv("../diabetes.csv")

dimensions = dataset.shape
print("Размеры набора данных по строкам и столбцам:", dimensions, end="\n\n")

first_5_rows = dataset.head(5)
print("Первые 5 строк набора данных:")
print(first_5_rows, end="\n\n")

last_10_rows = dataset.tail(10)
print("Последние 10 строк набора данных:")
print(last_10_rows, end="\n\n")

columns_names = dataset.columns.values
print(f"Названия столбцов набора данных: {', '.join(columns_names)}", end="\n\n")

print("Весь набор данных:")
print(dataset, end="\n\n")

print("Характеристики набора данных:")
dataset.info()
