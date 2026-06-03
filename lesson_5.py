# Задание 1

user_input = input('Введите число ')

if user_input.replace('-', '').isdigit():
    user_number = int(user_input)

    if user_number == 0:
        print('нулевое ', end='')
    else:
        if user_number > 0:
            print('положительное ', end='')
        else:
            print('отрицательное ', end='')
        if user_number % 2 == 0:
            print('четное ', end='')
        else:
            print('нечетное ', end='')
    print('число')
else:
    print('Некорректный ввод, ожидается целочисленое значение')

# Задание 2

lowel_letters_map = {'a': 0, 'e': 0, "i": 0, 'o': 0, 'u': 0}

user_word = input("Введите слово ")

count_consonat = 0

for letter in user_word:
    match letter:
        case 'a':
            lowel_letters_map['a'] += 1
        case 'e':
            lowel_letters_map['e'] += 1
        case 'i':
            lowel_letters_map['i'] += 1
        case 'o':
            lowel_letters_map['o'] += 1
        case 'u':
            lowel_letters_map['u'] += 1
        case _:
            count_consonat += 1

print(f'Количестко согласных букв {count_consonat}')
print('Гласные: ')

for key, value in lowel_letters_map.items():
    print(key, end=' ')
    print(value if value != 0 else 'False')

# Задание 3

min_invest, mike_invest, ivan_invest = int(
    input('Задайте минимальную инвестицию, сумму Майкла и сумму Ивана через пробел'))

if mike_invest >= min_invest and ivan_invest >= min_invest:
    print(2)
elif mike_invest >= min_invest:
    print('Mike')
elif ivan_invest >= min_invest:
    print('Ivan')
elif mike_invest + ivan_invest >= min_invest:
    print(1)
else:
    print(0)
