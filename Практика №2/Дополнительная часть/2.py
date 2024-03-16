print('Введите интересы первого и второго человека через пробел')
interests_of_person_1 = set(input().split())
interests_of_person_2 = set(input().split())

percent_of_common_interests = (len(interests_of_person_1 & interests_of_person_2)
                               / len(interests_of_person_1 | interests_of_person_2) * 100)

print(f'Общие интересы: {percent_of_common_interests:.2f}%')
