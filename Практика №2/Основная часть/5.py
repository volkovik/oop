first_word, second_word = input(), input()

letters = set(first_word) | set(second_word)

for letter in letters:
    if letter not in first_word or letter not in second_word:
        print('Слова не являются анограммами')
        break
else:
    print('Слова являются анограммами')
