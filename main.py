import random

# Генерація випадкового списку 3-10
random_length = random.randint(3, 10)
random_list = [random.randint(1, 10) for _ in range(random_length)]

# Створення нового списку з першого, третього та другого з кінця елементів
new_list = [random_list[0], random_list[2], random_list[-2]]

print("First list:", random_list)
print("Second list:", new_list)
