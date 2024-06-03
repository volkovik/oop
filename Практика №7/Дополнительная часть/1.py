import pandas as pd

dataset = pd.read_csv("../diabetes.csv")

dataset.rename(columns={"BloodPressure": "BloodPres", "Age": "YearsOld"}, inplace=True)
print("Переименованные столбцы:")
print(dataset)

dataset.drop(columns=["Outcome"], inplace=True)
print("Набор данных после удаления столбца 'Outcome':")
print(dataset)

sorted_dataset = dataset.sort_values(by="YearsOld", ascending=False)
print("Отсортированный набор данных по столбцу 'YearsOld':")
print(sorted_dataset)

filtered_dataset = dataset[dataset["BMI"] <= 24.9]
print("Отфильтрованный набор данных ('BMI' <= 24.9):")
print(filtered_dataset)
