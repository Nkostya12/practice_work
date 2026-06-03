# Задание 1
try:
    type_animal, age, name = input('Введите вид, кличку и возраст питомца через пробел ').split()
    print(f'Это {type_animal} по кличке "{name}". Возраст: {age}.')
except Exception as e:
    print("Некорректный ввод")

# Задание 2

stages = input('Введите этапы атропогенеза через запятую ').split(sep=',')

count = 0
for index, stage in enumerate(stages):
    match (stage.lower().strip(), index):
        case ('australopithecus', 0):
            count += 1
        case ('homo habilis', 1):
            count += 1
        case ('homo erectus', 2):
            count += 1
        case ('homo heidelbergensis', 3):
            count += 1
        case ('homo neanderthalensis', 4):
            count += 1
        case ('homo sapiens sapiens', 5):
            count += 1

print(*stages, sep=' => ')
print(f'Всего баллов: {count}')
