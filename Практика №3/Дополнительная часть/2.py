def split_text_into_nums_and_letters(text):
    nums = []
    letters = []
    for i in text:
        if i.isdigit():
            nums.append(i)
        else:
            letters.append(i)
    return nums, letters


text = input('Введите строку: ')

print(*split_text_into_nums_and_letters(text), sep='\n')