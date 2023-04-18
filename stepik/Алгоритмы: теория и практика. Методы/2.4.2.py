"""
Тест повышенной сложности: правильная скорость роста

Упорядочите данные функции по возрастанию скорости роста (сверху — медленнее всего растущая функция, снизу —
быстрее всего растущая).
https://stepik.org/lesson/O-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%B8%D0%BA%D0%B0-13230/step/10
"""

import math

n = 50

print()
print(math.log(math.log(n, 2), 10))
print(math.sqrt(math.log(n, 4)))
print(math.log(n, 3))

print()
print((math.log(n, 2)) ** 2)
print(math.sqrt(n))
print(n / math.log(n, 5))

print()
print(math.log(math.factorial(n), 2))
print(3 ** math.log(n, 2))
print(n ** 2)

print()
print(7 ** (math.log(n, 2)))
print(math.log(n, 2) ** (math.log(n, 2)))
print(n ** (math.log(n, 2)))

print()
print(n ** (math.sqrt(n)))
print(2 ** n)
print(4 ** n)

print()
print(2 ** (3 * n))
print(math.factorial(n))
# print(2 ** (2 ** n))


