import pandas as pd

dataset = pd.read_csv('../diabetes.csv')

rows_slice = dataset.iloc[3:8]
print("Срез строк по индексам (с 3 по 7):")
print(rows_slice)

columns_slice = dataset[['BMI']]
print("Срез столбцов по именам (только 'BMI'):")
print(columns_slice)
