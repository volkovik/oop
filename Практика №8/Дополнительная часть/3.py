import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../diabetes.csv')
diabetes = data[data['Outcome'] == 1]

bins = [0, 18.5, 25, 30, 35, 40, 100]
bmi_ranges = [
    sum(1 for x in diabetes['BMI'] if b_S <= x < b_E)
    for b_S, b_E in zip(bins[:-1], bins[1:])
]
labels_bmi = [f'{b_S}-{b_E}' for b_S, b_E in zip(bins[:-1], bins[1:])]

plt.figure(figsize=(10, 6))
plt.bar(labels_bmi, bmi_ranges)
plt.title('Diabetes BMI Distribution')
plt.xlabel('BMI Range')
plt.ylabel('Amount of People')
plt.show()
