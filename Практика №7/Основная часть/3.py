import pandas as pd

dataset = pd.read_csv('../diabetes.csv')

value_counts_bmi = dataset['BMI'][dataset['BMI'] == 33.3].value_counts()
print("Количество '3.33' в столбце 'BMI':")
print(value_counts_bmi)
