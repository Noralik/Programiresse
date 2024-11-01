massive_1 = ["максим", "М", 45, 64, 294]
massive_2 = ["никита", "М", 83, 82, 59]
massive_3 = ["катя", "Д", 392, 20, 25]

# Список всех массивов
all_massives = [massive_1, massive_2, massive_3]

# Проверяем каждый массив на наличие элемента "М" или "Д"
for massive in all_massives:
    if "М" in massive:
        print(massive)
    elif "Д" in massive:
        print(massive)
