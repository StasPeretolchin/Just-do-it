"""
Задача на программирование: небольшое число Фибоначчи

Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи (напомним, что F0 = 0, F1 = 1 и Fn-1 + Fn-2
при n ≥ 2).

https://stepik.org/lesson/13228/step/6?unit=3414
"""


# Мое решение
def fib(n):
    my_list = [0, 1]

    for i in range(2, n + 1):
        my_list.append(my_list[i - 1] + my_list[i - 2])

    return my_list[-1]


# Топ решение
def fib_top(n):
    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


def main():
    n = int(input())
    print(fib(n))
    print(fib_top(n))


if __name__ == "__main__":
    main()

