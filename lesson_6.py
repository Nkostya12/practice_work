# Задание 1

count_number = int(input('Введите количество чисел '))
print(f'Введите {count_number} чисел')

count_zero = 0

for number in range(0, count_number):
    if int(input(f'Введите число ')) == 0:
        count_zero += 1

print(f'Чисел равных нулю {count_zero}')

# Задание 2

user_input_number = int(input('Введите число '))

count_div = 0

for number, index in enumerate(range(1, user_input_number + 1)):
    if user_input_number % index == 0:
        count_div += 1

print(f'Количество натуральных делителей - {count_div}')

# Задание 3

number_a = int(input(f'Введите число А '))
number_b = int(input(f'Введите число B '))

if number_a > number_b:
    print('Число А должно быть меньше или равно B')
else:
    for number in range(number_a, number_b):
        if number % 2 == 0:
            print(number, end=' ')
