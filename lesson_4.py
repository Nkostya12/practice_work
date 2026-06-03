# Задание 1

def get_number(number_string):
    return float(number_string) if '.' in number_string or ',' in number_string else int(number_string)


print("""
          b 
      __________    
      |        |
   a  |        | c
      |________|
          d""")

values = input("Введите через пробел значение длины а, ширины b, длины c, ширины d ").split()

if len(values) < 4:
    print('Необходимо ввести 4 значения!')
else:

    values_number = list(map(lambda value: get_number(value), values))

    s = values_number[0] * values_number[1]
    p = values_number[0] + values_number[1] + values_number[2] + values_number[3]

    print(f'S = {s}\nP = {p}')

# Задание 2

user_input = input("Введите пятизначное число ")
if len(user_input) != 5:
    print('Число должно быть пятизначным')
else:
    numbers_float_list = list(map(lambda number_user: float(number_user), user_input))

    result = pow(numbers_float_list[3], numbers_float_list[4]) * numbers_float_list[2] / (
            numbers_float_list[0] - numbers_float_list[1])
    print(result)
