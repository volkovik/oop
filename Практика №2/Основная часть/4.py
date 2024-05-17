first_dict = {
    'first': 490,
    'second': 23,
}

second_dict = {"third": 59, }

third_dict = {
    "second": 12,
    "fourth": 29,
}

merged_dict = first_dict | second_dict | third_dict
merged_dict = {**first_dict, **second_dict, **third_dict}
print(f'Объединенный список: {merged_dict}')

sorted_merged_dict = dict(sorted(
    merged_dict.items(),
    key=lambda e: e[1]
))
print(f'По возрастанию: {sorted_merged_dict}')

reversed_sorted_merged_dict = dict(sorted(
    merged_dict.items(),
    key=lambda e: e[1],
    reverse=True
))
print(f'По убыванию: {reversed_sorted_merged_dict}')
