# Задание 1

input_user = input('Введите строку без пробелов ')
reverse_input_user = input_user[::-1]

print(input_user)
print(reverse_input_user)

if reverse_input_user == input_user:
    print('yes')
else:
    print('no')

# Задание 2

input_user = input('Введите строку ')
print(' '.join(input_user.split()))
